#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :settings.py
# @Time      :2022/01/20 14:57:09
# @Author    :hengdin


MODE = True

if MODE:
    settings = {
        "MYSQL": {
            "host": "127.0.0.1",
            "database": "locoy",
            "port": 3306,
            "user": "zyyt",
            "password": "Pwd@123.cn",
            "charset": 'utf8mb4'
        },
        "STORE_PATH":r"D:\news_data",
        "NEW_STORE_PATH":r"D:\package",
        # 2022-01-26 号 任务
        "NEW_STORE_PATH_26":r"D:/{}/数据文件/NEWS/DSJ_ZYRWFX_NEWS.csv",
        # 2022-01-26 号 任务 
        "NEW_ZIP_26":"{}.zip",
        "TABLE": "news_data",
        # 2022-01-26 号 任务
        "TABLE_26":"dsj_zyrwfx_news_translate",
        "ARTICLE_FILENAME":"articleData.txt",
        "PACKAGE":"package",
        "ZIP_NAME":"dataInfo.zip",
        "ZIP_STORE":r"D:\ZIP_STORE",
    }
else:
    settings = {
        "MYSQL": {
            "host": "127.0.0.1",
            "database": "test",
            "port": 3306,
            "user": "root",
            "password": "yongle95#",
            "charset": 'utf8mb4'
        },
        "STORE_PATH": r"D:\news_data",
        "NEW_STORE_PATH":r"D:\package",
        # 2022-01-26 号 任务
         "NEW_STORE_PATH_26":r"D:/{}/数据文件/NEWS/DSJ_ZYRWFX_NEWS.csv",
        # 2022-01-26 号 任务 
        "NEW_ZIP_26":"{}.zip",
        "TABLE": "news_data",
        # 2022-01-26 号 任务
        "TABLE_26":"dsj_zyrwfx_news_translate",
        "ARTICLE_FILENAME":"articleData.txt",
        "PACKAGE":"package",
        "ZIP_NAME":"dataInfo.zip",
        "ZIP_STORE":r"D:\ZIP_STORE",
    }


TEMPLATE = {

    "author": "",   #-------------------  
    "clickNumber": "0",    
    "comment": "",          #---------------
    "content": "",          #-----------------
    "contentForExport": "", 
    "contentShow": "",
    "contentTranslation": "",
    "creationTime": "2020-01-31 10:33:47", # ---------- 表自动生成
    "dataType": "1",
    "encoding": "UTF-8",
    #
    "excavateDataFileList": [  # ---------------------
        {
            "fileContent": "DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mxqsI9OmbSrC84uChTe1IdIK6OU6uRvhlrTKgsvY6muPXEc5Xlrafpg",
            "fileId": "1d64dfa643d211ea9a0ed2357b22748d",
            "fileName": "DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mxqsI9OmbSrC84uChTe1IdIK6OU6uRvhlrTKgsvY6muPXEc5Xlrafpg.jpg"  # -----------
        },
        {
            "fileContent": "DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mhFa21MTJZg4ebcWv7R54zDLogZt17HKfBibW5iabcXNCDcHR4f2eMFXQ",
            "fileId": "1d81a21a43d211ea8c2bd2357b22748d",
            "fileName": "DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mhFa21MTJZg4ebcWv7R54zDLogZt17HKfBibW5iabcXNCDcHR4f2eMFXQ.jpg"
        },
        {
            "fileContent": "DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mu7UszNZIFx6M2CMwsibiaLJDWF5W91hSbW4U7DJozEwgXgiaCJkFkiaribw",
            "fileId": "1d0cf4cc43d211eaa45bd2357b22748d",
            "fileName": "DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mu7UszNZIFx6M2CMwsibiaLJDWF5W91hSbW4U7DJozEwgXgiaCJkFkiaribw.jpg"
        },
        {
            "fileContent": "DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mB98ibLNJyhU9j9uMmCZELLM06T6eZBP9q2pw1iaMLnS48YrvVUd2kLAg",
            "fileId": "1cabccca43d211eab999d2357b22748d",
            "fileName": "DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mB98ibLNJyhU9j9uMmCZELLM06T6eZBP9q2pw1iaMLnS48YrvVUd2kLAg.jpg"
        },
        {
            "fileContent": "DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68m1d2fQHDicOEm0p3fNnYyAbaxEiaOibkT8t4WmRrxwx7ncMXnSbJPxcHLg",
            "fileId": "1c036a5243d211ea85c9d2357b22748d",
            "fileName": "DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68m1d2fQHDicOEm0p3fNnYyAbaxEiaOibkT8t4WmRrxwx7ncMXnSbJPxcHLg.jpg"
        },
        {
            "fileContent": "DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mYOzd91jo8m5ib1v2tpgOS2lJy2T7RHtazfXlqY7IylPjH80ecC2gg7Q",
            "fileId": "1bb981a843d211eabbfed2357b22748d",
            "path": "",
            "fileName": "DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mYOzd91jo8m5ib1v2tpgOS2lJy2T7RHtazfXlqY7IylPjH80ecC2gg7Q.jpg"
        }
    ],
    "guid": "1baeecf443d211eaacfdd2357b22748d", #!!!!!!!!!!!!!!!!!!!!!
    "imgList": [  # --------------------------------------------
        "https://mmbiz.qpic.cn/mmbiz_jpg/DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mYOzd91jo8m5ib1v2tpgOS2lJy2T7RHtazfXlqY7IylPjH80ecC2gg7Q/640?wx_fmt=jpeg",
        "https://mmbiz.qpic.cn/mmbiz_jpg/DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68m1d2fQHDicOEm0p3fNnYyAbaxEiaOibkT8t4WmRrxwx7ncMXnSbJPxcHLg/640?wx_fmt=jpeg",
        "https://mmbiz.qpic.cn/mmbiz_jpg/DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mB98ibLNJyhU9j9uMmCZELLM06T6eZBP9q2pw1iaMLnS48YrvVUd2kLAg/640?wx_fmt=jpeg",
        "https://mmbiz.qpic.cn/mmbiz_jpg/DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mu7UszNZIFx6M2CMwsibiaLJDWF5W91hSbW4U7DJozEwgXgiaCJkFkiaribw/640?wx_fmt=jpeg",
        "https://mmbiz.qpic.cn/mmbiz_jpg/DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mxqsI9OmbSrC84uChTe1IdIK6OU6uRvhlrTKgsvY6muPXEc5Xlrafpg/640?wx_fmt=jpeg",
        "https://mmbiz.qpic.cn/mmbiz_jpg/DhKPeHFI5HiayN8r9KVkbZEQ6rUKGu68mhFa21MTJZg4ebcWv7R54zDLogZt17HKfBibW5iabcXNCDcHR4f2eMFXQ/640?wx_fmt=jpeg",
        "https://mmbiz.qpic.cn/mmbiz_gif/DhKPeHFI5HiaNP2NtUoI7Ub3rpk4uGiagUtk3ajsTp6PsRuASJF7bfksQTGjWTm3CXtuhibNePwCQcibxCicEqAkhpw/640?wx_fmt=gif"
    ],
    "keywords": "",  # ---------------------
    "metaData": "",
    "publicDate": "2020-01-30$yyyy-MM-dd",# --------------------- +++++++++++++++++++
    "publicDateTime": "2020-01-30 09:32:31",# -------------------  +++++++++++++++++++++++
    "publicTime": "",  # 空
    "refernceUrl": "https://mp.weixin.qq.com/",  # ----------------
    "region": "China",  # --------------
    "replies": "",     # 空
    "reproduced": "",  # 空
    "siteCofId": "4434b29c40ab46b796c64062142e2c32",  # -----------------
    "siteCofName": "共产党员",  # -------------------
    "taskDataId": "",  # 空
    "title": "最新疫情报告: 确诊7711例 死亡170例 治愈124例",  # ----------------
    "titleTranslation": "",
    "url": "86c7864e006c943#rd",  # ---------------------
    "videoList": []
}
