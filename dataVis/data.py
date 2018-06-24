# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-04-22'

from numpy import array
from numpy.random import normal
from dataVis.webUI import data_web_ui
import link_mongodb

# 假定用户输入两个关键词，要求统计，接收到的数据应该是{'k1':[],'k2':[]}
def handleData(keyword_list):
    #假定我们已经获取到了关键词
    print(keyword_list)#['华为'，'小米']
    sheet = link_mongodb.linkMongoDB()
    content = []
    data_dict = {}
    for keyword in keyword_list:
        data_dict[keyword] = []
        data_list_temp = []
        cont_temp = sheet.find({'keyword': {'$in': [keyword]}})
        # print(cont_temp)
        for content_temp in cont_temp:
            content.append('标题:'+content_temp['title']+'  \t 部门：'+content_temp['target']+'  \t 内容：'+content_temp['content']+'   \t'+content_temp['date']+'\n')
            data_list_temp.append(content_temp['date'].split()[1])
        data_dict[keyword] = data_list_temp
    #返回值data_dict模板
    # data_dict = {'华为': ['00:12:12', '03:12:12', '03:12:12', '06:12:12', '09:12:12', '00:12:12', '20:12:12', '15:12:12',
    #                     '19:12:12'],
    #              '小米': ['01:12:12', '03:12:12', '13:12:12', '12:12:12', '19:12:12', '00:12:12', '21:12:12', '05:12:12',
    #                     '09:12:12']}
    return [data_dict,content]


def getData(data_dict):
    # handleData(keyword_list)
    data_keyword_sum = {}
    for k in  data_dict:
        type_data = []
        # print(k)
        for d in data_dict[k]:
            if d > '00:00:00' and d < '24:00:00':
                data = '0~4' if d < '04:00:00' else ('4~8' if d < '08:00:00' else
                                                       ('8~12' if d < '12:00:00' else ('12~16' if d < '16:00:00'
                                                          else ('16~20' if d < '20:00:00' else '20~24'))))
            type_data.append(data)
        data_keyword_sum[k] = type_data
    return data_keyword_sum

def main(keyword_list):
    # keyword_list = ['临清']
    [data_dict,content]=handleData(keyword_list)
    # print('data_dict:' + str(data_dict))
    data_keyword_sum=getData(data_dict)
    return [data_keyword_sum,content]


if __name__ == '__main__':
    # grades = getData()
    # print(grades)
    # keyword_list = data_web_ui.MainPageHandler.text()
    keyword_list = ['丁','月','星']
    # handleData(keyword_list)
    main(keyword_list)