from socket import IPV6_CHECKSUM
import traceback
import requests
import json
from utils.pipelines import MysqlPipeline
from settings import settings
from traceback import  format_exc
from jsonpath import jsonpath
import time
from pymysql.converters import escape_string

API = settings["API"]

TABLE_NEWS = settings["TABLE_NEWS"]
TABLE_PERSON = settings["TABLE_PERSON"]


class Api_translation:


    def __init__(self) -> None:
        self.pipeline = MysqlPipeline()
        self.select_sql_news = 'select id,title,content,srcl from `{}` where (contentTranslation is null  or titleTranslation is null) and srcl != "zh" ;'.format(TABLE_NEWS)
        self.select_sql_person = 'select id,title,content,srcl from `{}` where (title_cn is null or content_cn is null) and srcl != "zh" ;'.format(TABLE_PERSON)
        
        self.update_sql_news  = """ UPDATE `{}` SET `titleTranslation`=%s,`contentTranslation`=%s where id=%s; """.format(TABLE_NEWS)
        self.update_sql_person  = """ UPDATE `{}` SET `title_cn`=%s,`content_cn`= %s where id=%s; """.format(TABLE_PERSON)


    def request_to_api(self,srcl,text):
        """
        调用 翻译 api
        """
        parameters = {
            "srcl":"n{}".format(srcl), # 原文 英文
            "tgtl":"nzh", #  目标 中文 # string 或者 array
            "text":text
        }
        # 存在 title 或者 content 为空的情况 
        if not text:
            return ''

        for i in range(20):
            try:
                resp = requests.post(API,data = json.dumps(parameters),timeout=60)
                time.sleep(1)
                return resp.json()
            except:
                print(text)
                print(resp.text)
                print(format_exc())
        return None

    def extract(self,obj):
        """
        解析API 返回的json 数据,提取翻译后的结果
        
        """
        try:
            text = jsonpath(obj,'$..text')[0]
            return text
        except:

            print(format_exc())
            return None



    def handle_item(self,tup):
        """
        将查询到的 元组数据 整理成 dict 格式
        """
        item = {}
        item["id"] = tup[0] # -------------
        item["title"] = tup[1]       # -------------
        item["content"] = tup[2]     # -------------
        item["srcl"] = tup[3]        # -------------
        return item

    def handle_translate(self,item):
        """
        处理 title,content 的请求  

        处理前 : 
        item ={
            "id":"",
            "title":"",
            "content":"",
            "srcl":"",
        }
        处理后: 
        item ={
            "id":"",
            "title":"",
            "content":"",
            "srcl":"",
            "title_translate":"",
            "content_translate":"",
        
        }
        """
        resp_title = self.request_to_api(item["srcl"],item["title"])
        if resp_title:
            title_translate = self.extract(resp_title)
        else:
            title_translate = ''

        resp_content = self.request_to_api(item["srcl"],item["content"])
        if resp_content:
            content_translate = self.extract(resp_content)
        else:
            content_translate = ''

        item["title_translate"] = title_translate 
        item["content_translate"] = content_translate 
        # print("原标题: {}, 翻译标题: {}".format(item["title"],item["title_translate"]))
        # print("原文: {}, 译文: {}".format(item["content"],item["content_translate"]))
        return item

    def gen_update_sql(self,item,update_sql_):
        """
        利用 item 生成 update的sql
        """
        update_sql = update_sql_.format(escape_string(item["title_translate"]),escape_string(item["content_translate"]),item["id"])
        return update_sql

    def gen_update_val(self,item):
        """
        利用 item 生成 update的sql
        """
        val = (item["title_translate"],item["content_translate"],item["id"])
        return val

    def work(self,select_sql,update_sql):
        """
        处理人物表
        """
        item_list = self.pipeline.select_items(select_sql)
        for item_tup in item_list:
            item = self.handle_item(item_tup)
            item = self.handle_translate(item)
            val = self.gen_update_val(item)
            self.pipeline.update(update_sql,val)

    def run(self):
        # 处理 新闻的翻译 
        self.work(self.select_sql_news,self.update_sql_news)

        # 处理 任务的翻译
        self.work(self.select_sql_person,self.update_sql_person)


if __name__ =="__main__":
    ts = Api_translation()
    ts.run()