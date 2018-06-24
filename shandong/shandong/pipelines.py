# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import pymongo
from shandong.shandong import settings


class ShandongPipeline(object):
    def __init__(self):
        # self.filename = codecs.open('sun_reply_shandong.json','w',encoding='utf-8')
        # 数据库接口
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        dbname = settings.MONGODB_DBNAME
        sheet = settings.MONGODB_SHEET
        # 创建数据库客户端
        client = pymongo.MongoClient(host=host,port=port)
        mongdb = client[dbname]
        # 创建表对象
        self.sheet = mongdb[sheet]


    def process_item(self, item, spider):
        data = dict(item)
        # # 爬虫存入本地文件
        # jsonlist = json.dumps(data,ensure_ascii=False)+'\n'
        # self.filename.write(jsonlist)

        # 爬虫入库
        self.sheet.insert(data)
        return item

    # def close_spider(self):
    #     self.filename.close()
