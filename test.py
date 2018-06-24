# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-00-00'

import pymongo

client = pymongo.MongoClient("localhost",27017)
dbname = 'SUNSHAHINE'
db = client[dbname]
sheet = db.BBS
keyword = '临清'
tip = {'keyword':{'$in':[keyword]}}
list_mongodb = sheet.find({'keyword':{'$in':[keyword]}})
print(list_mongodb)
for data in list_mongodb:
    print(type(data))
    print(data['keyword'])