#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2022/01/20 14:55:55
# @Author    :hengdin
from utils.utils import *
from settings import TEMPLATE, settings
from pipelines import MysqlPipeline
from traceback import format_exc
from copy import deepcopy
import time
import json
import os
import sys

sys.path.append(dir(__file__))
# print(sys.path)

TABLE = "dsj_zyrwfx_news_translate"
PACKAGE = settings["PACKAGE"]

STORE_PATH = settings['STORE_PATH']

NEW_STORE_PATH_FILE = settings['NEW_STORE_PATH_PERSON']

class Main:
    def __init__(self):
        self.pipeline = MysqlPipeline(TABLE)
        self.li = []
        self.fileds = [
            "id",
            "person_id",
            "website_source",
            "website_domain",
            "Website_type",
            "language",
            "author",
            "news_type",
            "data_source_url",
            "title",
            "title_cn",
            "content",
            "content_cn",
            "publish_time",
            "comment_count",
            "read_count",
            "image_url",
            "video_url",
            "image_org_url",
            "video_cover",
            "video_org_url",
            "original_tags",
            "original_keywords",
            "is_retweeted",
            "repost_source",
            "repost_platform_name",
            "plate_ platform_url",
            "if_front_position",
            "special_name",
            "special_keyword",
            "create_time"
        ]

    def process_json(self, item):
        """
        将一条数据生成一个单独的数据
        """
        item = list(item)
        id_ = item[0]
        li = []
        for i in item:
            if not i:
                i=''
            i= str(i)
            li.append(i)
        li_str = "\001".join(li)
        return id_,li_str

    def run(self):
        """
        程序主入口
        """
        current_date = time.strftime(
            r"%Y%m%d", time.localtime(int(time.time())))
        file_path = NEW_STORE_PATH_FILE.format(current_date)
        STORE_PATH_DIR  = os.path.dirname(file_path)
        if not os.path.exists(STORE_PATH_DIR):
            os.makedirs(STORE_PATH_DIR)

        item_list = self.pipeline.select_items()
        with open(file_path,'w',encoding= "utf-8")as f:
            # 第一行写入 数据库表 字段
            fileds_str = "\001".join(self.fileds)
            f.write(fileds_str)
            for item in item_list:
                # 1 先整理为 list 格式
                f.write("\n")
                id_,li_str = self.process_json(item)
                f.write(li_str)
                
                # 修改mysql 中的状态
                self.pipeline.update_tag(id_)

        zip_dir_person(current_date,file_path)


if __name__ == "__main__":
    m = Main()
    m.run()
