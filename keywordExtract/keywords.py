# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-00-00'


import jieba
import jieba.analyse


top_num = 30

def getTopic():
    with open('text.txt','r',encoding='utf-8')as f:
        content = f.read()
    tags = jieba.analyse.extract_tags(content,40)
    print(tags)

if __name__ == '__main__':
    getTopic()