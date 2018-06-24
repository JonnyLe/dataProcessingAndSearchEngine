# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-04-29'

#导入高级（精确）搜索模块
from bigDataIndex import SplunkM
#导入初级（模糊）搜索模块
from bigDataIndex import Splunk
#导入数据库连接函数
from link_mongodb import linkMongoDB
#导入画图处理模块
from dataVis import data


def data_handle(keyword_list):
    #模糊查找实例对象
    s = Splunk.Splunk()
    #准确查找实例对象
    sm = SplunkM.SplunkM()
    datahouse = linkMongoDB().find()
    i = 1
    #临时存储用户数据
    data_list = []
    content = []
    data_kw_dict = {}
    for kw in keyword_list:
        data_kw_dict[kw] = []
    for data in datahouse:
        # print('data:'+str(data))
        if i % 64 == 0:
            print('i:'+str(i))
            for d in data_list:
                if str(d['keyword']) in sm.search_any(keyword_list):
                    # print('hahhahhahhhah')
                    for kw in keyword_list:
                        if kw in d['keyword']:
                            data_kw_dict[kw].append(d['date'].split()[1])
                    content.append('标题:' + d['title'] + '  \t 部门：' + d['target'] + '  \t 内容：' + d['content']
                                   + '   \t' + d['date'] + '\n')
                    # print('content:' + str(content))
            sm = SplunkM.SplunkM()
            data_list = []
        data_list.append(data)
        sm.add_event(str(data['keyword']))
        # print('data_list:'+str(data_list))
        i += 1
    return [data_kw_dict,content]


def main(keyword_list):
    [data_kw_dict,content] = data_handle(keyword_list)
    # print('data_kw_dict:' + str(data_kw_dict))
    data_keyword_sum = data.getData(data_kw_dict)
    return [data_keyword_sum, content]


if __name__ == '__main__':
    keyword_list = ['济南','临清']
    [data_keyword_sum, content]=main(keyword_list)
    print('data_keyword_sum:' + str(data_keyword_sum))
    # print('content:' + str(content))