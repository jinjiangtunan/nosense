# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

import os
import time
import traceback
import pymysql
from traceback import format_exc
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
from settings import settings,TEMPLATE




MYSQL_SETTINGS = settings["MYSQL"]



class MysqlPipeline:
    """
    保存数据进mysql
    """

    def __init__(self,table):
        """
        链接数据库
        """
        self.table =table
        self.host = MYSQL_SETTINGS["host"]
        self.init_connect()
        self.select_unhandled_sql = '''select * from {} where tag=0 ; '''.format(table)
        
    def init_connect(self):
        while True:
            try:
                self.conn = pymysql.connect(**MYSQL_SETTINGS)
                self.cursor = self.conn.cursor()
                print("mysql数据库 -{}- 连接成功".format(self.host))
                return True
            except:
                print("数据库: {} 链接失败...".format(self.host))
                time.sleep(10)

    def select_items(self,select_sql):
        """
        负责执行一次数据查询操作,并返回查询结果
        """
        
        try:
            self.conn.ping()
            self.cursor.execute(select_sql)
            self.conn.commit()
            item_list = self.cursor.fetchall()
            print('数据库查询成功,查询到 {} 条待处理 数据...'.format(len(item_list)))
            return item_list

        except Exception as e:
            # print('数据库错误(其他)  请查看\n{}\n{}'.format(format_exc(), item), WARNING)
            print('数据库错误(其他)  请查看\n{}'.format(format_exc()))
            
            return []
    
        
    def update_tag(self,table,id_):
        
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except:
            print(traceback.format_exc())
        


if __name__ =="__main__":
    a= MysqlPipeline()
    a.run()
