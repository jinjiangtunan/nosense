#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2022/01/20 14:55:55
# @Author    :hengdin
import os
import sys
from pprint import pprint
sys.path.append(dir(__file__))
print(sys.path)
import json
import time
from copy import deepcopy
from traceback import format_exc

from pipelines import MysqlPipeline
from settings import TEMPLATE, settings
from utils.utils import *


PACKAGE = settings["PACKAGE"]

STORE_PATH = settings['STORE_PATH']

NEW_STORE_PATH =  settings['NEW_STORE_PATH']

TABLE = settings["TABLE"]

class Main:
    def __init__(self):
        self.pipeline = MysqlPipeline(TABLE)
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
        meta["contentTranslation"] = item[4]
        meta["creationTime"] = str(item[5])
        meta["excavateDataFileList"] = handle_files(item[6])
        meta["guid"] = handle_guid(str(meta["author"])+meta["content"]+str(meta["creationTime"])+meta["title"]+meta["siteCofName"])
        meta["imgList"] =  [item[7]]
        meta["keywords"] = item[8]
        print("处理前：{}".format(item[9]))
        
        publicDate = date_extract(item[9])
        meta["publicDate"] = publicDate +"$yyyy-MM-dd" if publicDate else str(item[9])
        print("处理后：{}".format(meta["publicDate"]))
        if not "$yyyy-MM-dd" in meta["publicDate"]:
            print(meta["publicDate"])
        
        
        publicDateTime = time_extract(item[10])
        
        meta["publicDateTime"] = publicDateTime if publicDateTime else str(item[10])
        meta["refernceUrl"] = item[11]
        meta["region"] = item[12]
        meta["siteCofId"] = item[13]
        meta["siteCofName"] = item[14]
        meta["title"] = item[15]
        meta["titleTranslation"] = item[16]
        meta["url"] = item[17]

        return id_,meta

    def run(self):
        """
        程序主入口
        """
        if not os.path.exists(NEW_STORE_PATH):
            os.makedirs(NEW_STORE_PATH)
        else:
            print("开始删除....")
            del_file(NEW_STORE_PATH)
            print("删除结束....")
        
        # while 1:
        all_file_paths = []
        # 先获取全部的文件绝对路径
        gen_allfile_path(STORE_PATH,all_file_paths)

        print("得到的所有文件: {}".format(all_file_paths))
        current_date = time.strftime(r"%Y-%m-%d",time.localtime(int(time.time())))
        
        item_list = self.pipeline.select_items()
        for item in item_list:
            # print("原始数据：{}".format(item))
            # 1 先整理为json 格式
            id_,meta = self.process_json(item)
            # print("整理后的数据： {}".format(meta))
            # 2 生成对应文章文件夹
            article_dir = gen_article_dir(NEW_STORE_PATH,meta["guid"])
            # 3 找到对应的文件。
            gen_article_file(all_file_paths,meta,article_dir)
            # 将json 写入进去
            article_file_name = gen_article_content_path(article_dir)
            try:
                with open(article_file_name,'w',encoding="utf-8")as f:
                    json.dump(meta,f,ensure_ascii=False)
            except:
                pprint(meta)
                for k,v in meta.items():
                    print(type(v))
                print(format_exc())
            # 修改mysql 中的状态
            self.pipeline.update_tag(id_)

        be_zip_dir = os.path.join(NEW_STORE_PATH)
        zip_dir(be_zip_dir,current_date)
            
            
            
if __name__ =="__main__":
    m= Main()
    m.run()