#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2022/01/20 14:55:55
# @Author    :hengdin
import os
import sys

sys.path.append(dir(__file__))
print(sys.path)
import json
import time
from copy import deepcopy

from utils.pipelines import MysqlPipeline
from settings import TEMPLATE, settings
from utils.utils import *

TABLE = settings['TABLE_NEWS']

PACKAGE = settings["PACKAGE"]

STORE_PATH = settings['STORE_PATH']

NEW_STORE_PATH =  settings['NEW_STORE_PATH']

class Main:
    def __init__(self):
        self.select_sql = '''select * from {} where  tag=0 and ((contentTranslation is not null and titleTranslation is not null) or srcl="zh") and  publicDate is not  null and publicDateTime is not null; '''.format(TABLE)
        self.update_sql = """ UPDATE {} SET tag=1 where id=%s """ 
        self.pipeline = MysqlPipeline()
        self.li = []

    def process_json(self,item):
        """
        将一条数据生成一个单独的数据
        """
        id_ = item[0]
        meta = deepcopy(TEMPLATE)
        meta["author"] = item[1]
        meta["comment"] =item[2] if item[2] else ''
        meta["content"] = item[3]
        meta["contentTranslation"] = item[4] if item[4] else ''
        meta["creationTime"] = str(item[5])
        
        meta["excavateDataFileList"] = handle_files(item[6])
        meta["guid"] = handle_guid(str(meta["author"])+meta["content"]+str(meta["creationTime"])+meta["title"]+meta["siteCofName"])
        meta["imgList"] =  [item[7]]
        meta["keywords"] = item[8]
         
        meta["publicDate"] = item[10]        
        meta["publicDateTime"] = item[11]
        meta["refernceUrl"] = item[12]
        meta["region"] = item[13]
        meta["siteCofId"] = item[14]
        meta["siteCofName"] = item[15]
        meta["title"] = item[16]
        meta["titleTranslation"] = item[17]
        meta["url"] = item[18]

        return id_,meta

    def run(self):
        """
        程序主入口
        """
        if not os.path.exists(NEW_STORE_PATH):
            os.makedirs(NEW_STORE_PATH)


        # while 1:
        all_file_paths = []
        # 先获取全部的文件绝对路径
        gen_allfile_path(STORE_PATH,all_file_paths)

        print("得到的所有文件: {}".format(all_file_paths))
        current_date = time.strftime(r"%Y-%m-%d",time.localtime(int(time.time())))
        
        
        item_list = self.pipeline.select_items(self.select_sql)
        for item in item_list:
            # 1 先整理为json 格式
            res = self.process_json(item)
            if not res:
                continue
            id_,meta = res
            # 2 生成对应文章文件夹
            article_dir = gen_article_dir(NEW_STORE_PATH,meta["guid"])
            # 3 找到对应的文件。
            gen_article_file(all_file_paths,meta,article_dir)
            # 将json 写入进去
            article_file_name = gen_article_content_path(article_dir)
            with open(article_file_name,'w',encoding="utf-8")as f:
                json.dump(meta,f,ensure_ascii=False)
            # 修改mysql 中的状态
            val= (id_)
            update_sql = self.update_sql.format(TABLE)
            self.pipeline.update(update_sql,val)

        be_zip_dir = os.path.join(NEW_STORE_PATH)
        zip_dir(be_zip_dir,current_date)
            
            
            
if __name__ =="__main__":
    m= Main()
    m.run()