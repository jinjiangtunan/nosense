#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :utils.py
# @Time      :2022/01/20 18:33:54
# @Author    :hengdin

import hashlib
from traceback import format_exc
from settings import settings
import os
import zipfile
import requests
import json
import re
import time

ARTICLE_FILENAME = settings["ARTICLE_FILENAME"]
PACKAGE = settings["PACKAGE"]
ZIP_NAME = settings["ZIP_NAME"]
ZIP_STORE = settings["ZIP_STORE"]
NEW_ZIP_PERSON = settings["NEW_ZIP_PERSON"]
TIME_TRANSFER_API = settings["TIME_TRANSFER_API"]

def handle_files(excavateDataFileList):
    """
    根据给到的附件文件名 ,生成其md5值 
    excavateDataFileList
    """
    fileContent = excavateDataFileList.split('.')[0]
    # 找到文件，对文件内容进行md5
    fileId = hashlib.md5(excavateDataFileList.encode()).hexdigest()
    fileName = excavateDataFileList

    li = [{
        "fileContent": fileContent,
        "fileId": fileId,
        "fileName": fileName
    }]
    return li


def gen_allfile_path(dir_path, li):
    inner_list = os.listdir(dir_path)
    for i in inner_list:

        i_path = os.path.join(dir_path, i)
        if os.path.isdir(i_path):
            gen_allfile_path(i_path, li)

        else:
            li.append(i_path)


def gen_article_file(abs_li, meta, article_path):
    """
    获取绝对路径的列表 ，从中筛选 当前 文章的 附件 ，并拷贝到该文章对应的文件夹下
    - abs_li STORE_PATH 下所有文件的绝对路径
    - meta 文章item
    - article_path 文章item 对应的文件夹
    """
    for path_ in abs_li:
        file_ = os.path.basename(path_)  # 带后缀的文件名
        if file_ == meta["excavateDataFileList"][0]["fileName"] or file_ == meta["imgList"][0]:
            new_file_path = os.path.join(article_path, file_)
            with open(path_, 'rb')as f:
                content = f.read()

                with open(new_file_path, 'wb')as ff:
                    ff.write(content)
                    print("已完成从: {} --->  {} 的复制 ....".format(path_, new_file_path))


def handle_guid(text):
    """
    生成 text的md5消息摘要结果。并返回。
    text 为 作者，content，title等字段组合体。
    """
    return hashlib.md5(text.encode()).hexdigest()


def gen_article_dir(root_dir,path_article):
    """
    生成文章对应的文件夹
    - root_dir  根路径
    - path_date 当前日期   
    - path_article 文章md5值
    """
    path_ = os.path.join(root_dir,  path_article)

    if not os.path.exists(path_):
        os.makedirs(path_)
    return path_


def gen_article_content_path(article_dir):
    return os.path.join(article_dir, ARTICLE_FILENAME)


def zip_dir(dir, current_date):
    """
    压缩文件夹内的文件 
    - dir 被压缩的文件夹
    - current_date 给定的日期
    """
    if not os.path.exists(ZIP_STORE):
        os.makedirs(ZIP_STORE)

    file_list = []
    gen_allfile_path(dir, file_list)
    zip_file_name = "{}_{}".format(current_date, ZIP_NAME)
    target_path = os.path.join(ZIP_STORE, zip_file_name)
    f = zipfile.ZipFile(target_path, 'w', zipfile.ZIP_DEFLATED)
    for file_ in file_list:
        f.write(file_)
    f.close()
    print("生成了 ZIP 文件:{}".format(target_path))
    
def zip_dir_person(current_date,file):
    """
    压缩文件夹内的文件 
    - dir 被压缩的文件夹
    - current_date 给定的日期
    """
    if not os.path.exists(ZIP_STORE):
        os.makedirs(ZIP_STORE)

    zip_file_name = NEW_ZIP_PERSON.format(current_date)
    target_path = os.path.join(ZIP_STORE, zip_file_name)
    f = zipfile.ZipFile(target_path, 'w', zipfile.ZIP_DEFLATED)
    
    f.write(file)
    f.close()
    print("生成了 ZIP 文件:{}".format(target_path))


def time_transfer(origin_pubtime,time_diff):
    """
    origin_pubtime  原始发布时间
    time_diff   时间差

    请求接口  得到时间  
    然后 处理 
    """
    parameters ={
        "time":origin_pubtime
    }

    headers = {
                "Content-Type": "application/json"
    }
    try:
        resp = requests.post(TIME_TRANSFER_API,headers=headers,data = json.dumps(parameters))
        res = resp.json()
        if res["code"] == 20000:
            time_stamp =  (res["data"]/1000 )+(time_diff*60*60)
            return time.strftime(r"%Y-%m-%d %H:%M:%S",time.localtime(time_stamp))
        else:
            return None
    except:
        print(format_exc())

def time_transfer_test(origin_pubtime,time_diff):
    """
    """
    try:
        print("原始：{}".format(origin_pubtime))
        res = re.findall(r'(20\d{2}-\d{2}-\d{2}).*?(\d{2}:\d{2}:\d{2}).*',origin_pubtime)
        print(res)
        
        publicDateTime = ' '.join(res[0])
        print("jieguoweo :{}".format(publicDateTime))

        time_stamp = time.mktime(time.strptime(publicDateTime,r"%Y-%m-%d %H:%M:%S"))
        time_stamp = time_stamp + time_diff*60*60
        return time_stamp
    except:
        print(format_exc())

def date_extract_test(time_stamp):
    return time.strftime(r"%Y-%m-%d",time.localtime(time_stamp))

def datetime_extract(time_stamp):
    return time.strftime(r"%Y-%m-%d %H:%M:%S",time.localtime(time_stamp))




def time_extract(time_str):
    time_str = str(time_str)
    try:
        res = re.findall(r'(20\d{2}-\d{2}-\d{2}).*?(\d{2}:\d{2}:\d{2})',time_str)
        res = [i[0] for i in res]
        publicDateTime = ' '.join(res)
        return publicDateTime
    except:
        print(format_exc())
        return None
    
def date_extract(date_str):
    try:
        publicDate = date_str.split(" ")[0]
        return publicDate
    except:
        print(format_exc())
        return None


if __name__ == "__main__":
    a = "hehe"
    b = "bb"
    p = gen_article_dir(r"D:\congress\117\crec\2021\01\13", a, b)
    p = gen_article_dir(r"D:\congress\117\crec\2021\01\13", a, b)
    
