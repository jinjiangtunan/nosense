from socket import IPV6_CHECKSUM
import traceback
import requests
import json
from utils.pipelines import MysqlPipeline
from settings import settings
from traceback import  format_exc
from jsonpath import jsonpath
import time
from utils.utils import date_extract
API = settings["API"]

TABLE_NEWS = settings["TABLE_NEWS"]
TABLE_PERSON = settings["TABLE_PERSON"]


TIME_TRANSFER_API = settings["TIME_TRANSFER_API"]

class Api_time_transfer:

    def __init__(self) -> None:
        self.pipeline = MysqlPipeline()
        self.select_sql_news = 'select id,pubtime,time_diff,creationTime from `{}` where publicDate is null  or publicDateTime is null;'.format(TABLE_NEWS)
        self.select_sql_person = 'select id,pubtime,time_diff,create_time from `{}` where publish_time is null ;'.format(TABLE_PERSON)
        
        self.update_sql_news  = """ UPDATE `{}` SET `publicDate`=%s,`publicDateTime`=%s where id=%s; """.format(TABLE_NEWS)
        self.update_sql_person  = """ UPDATE `{}` SET `publish_time`=%s where id=%s; """.format(TABLE_PERSON)


    def time_transfer(self,origin_pubtime,time_diff):
        """
        origin_pubtime  原始发布时间
        time_diff   时间差

        请求接口  得到时间  
        然后 处理 
        """
        if not origin_pubtime:
            return None

        parameters ={
            "time":origin_pubtime
        }

        headers = {
                    "Content-Type": "application/json"
        }
        try:
            start = int(time.time())
            print("开始请求....")
            resp = requests.post(TIME_TRANSFER_API,headers=headers,data = json.dumps(parameters))
            end = int(time.time())
            print("耗时：{}".format(end-start))
            res = resp.json()
            if res["code"] == 20000:
                time_stamp =  (res["data"]/1000 )+(time_diff*60*60)
                return time.strftime(r"%Y-%m-%d %H:%M:%S",time.localtime(time_stamp))
            else:
                return None
        except:
            print(format_exc())


    def handle_item(self,item_tup):

        item={
            "id":item_tup[0],
            "origin_pubtime":item_tup[1],
            "time_diff":item_tup[2],
            "creationTime":item_tup[3]
        }
        return item


    def work(self,select_sql,update_sql):
        """
        处理人物表
        """
        # 查询出数据
        item_list = self.pipeline.select_items(select_sql)
        for item_tup in item_list:
            # 整理数据格式
            item = self.handle_item(item_tup)
            # 得到 接口转换后的时间
            transfered_datetime = self.time_transfer(item["origin_pubtime"],item["time_diff"])
            # 转换失败后 使用 入库时间代替
            if not transfered_datetime:
                transfered_datetime = str(item["creationTime"])

            publicDate = date_extract(transfered_datetime)
            
            item["publicDate"] = publicDate +"$yyyy-MM-dd" 
        
            item["publicDateTime"] = transfered_datetime

            if TABLE_NEWS in update_sql:
                val = (item["publicDate"],item["publicDateTime"],item["id"])
            else:
                val =  (item["publicDateTime"],item["id"])

            self.pipeline.update(update_sql,val)

    def run(self):
        # 处理 新闻的翻译 
        self.work(self.select_sql_news,self.update_sql_news)

        # 处理 任务的翻译
        self.work(self.select_sql_person,self.update_sql_person)


if __name__ =="__main__":
    ts = Api_time_transfer()
    ts.run()