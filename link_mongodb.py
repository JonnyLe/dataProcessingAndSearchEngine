# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-04-27'

import pymongo
def linkMongoDB():
    client = pymongo.MongoClient("localhost",27017)
    dbname = 'SUNSHAHINE'
    db = client[dbname]
    sheet = db.BBS
    return sheet

