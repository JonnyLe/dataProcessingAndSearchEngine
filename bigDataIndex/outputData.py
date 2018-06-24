# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-04-26'


import pymongo
from shandong.shandong import settings
from bigDataIndex import SplunkM
from dataVis.webUI import data_web_ui
from shandong.shandong import pipelines

def getDataFromMongo(keyword):
    client = pymongo.MongoClient("localhost", 27017)
    dbname = 'SUNSHAHINE'
    db = client[dbname]
    sheet = db.BBS
    list_data = sheet.find({'keyword':{'$in':[keyword]}})



if __name__ == '__main__':
    getDataFromMongo()
