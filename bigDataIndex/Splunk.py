# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-04-24'

# 有个分词和布隆过滤器这两个利器的支撑后，我们就可以来实现搜索的功能
# Splunk代表一个拥有搜索功能的索引集合
#
# 每一个集合中包含一个布隆过滤器，一个倒排词表（字典），和一个存储所有事件的数组
#
# 当一个事件被加入到索引的时候，会做以下的逻辑
#
# 为每一个事件生成一个unqie id，这里就是序号
# 对事件进行分词，把每一个词加入到倒排词表，也就是每一个词对应的事件的id的映射结构，注意，一个词可能对应多个事件，所以倒排表的的值是一个Set。倒排表是绝大部分搜索引擎的核心功能。
# 当一个词被搜索的时候，会做以下的逻辑
#
# 检查布隆过滤器，如果为假，直接返回
# 检查词表，如果被搜索单词不在词表中，直接返回
# 在倒排表中找到所有对应的事件id，然后返回事件的内容
from bigDataIndex import BloomFilter
from bigDataIndex import segments
class Splunk(object):
    def __init__(self):
        self.bf = BloomFilter.bloomfilter(64)
        self.terms = {}  # Dictionary of term to set of events
        self.events = []

    def add_event(self, event):
        """添加元素到这个对象中"""

        # 为事件生成一个惟一的ID，并保存它
        event_id = len(self.events)
        self.events.append(event)

        # 将每个事件添加到bloomfilter中，并逐项跟踪事件
        for term in segments.segments(event):
            self.bf.add_value(term)

            if term not in self.terms:
                self.terms[term] = set()
            self.terms[term].add(event_id)

    def search(self, term):
        """搜索一个单独的术语，并生成包含它的所有事件"""

        # 在Splunk中，这在O（1）内运行，并且很可能在文件系统缓存中 (memory)
        if not self.bf.might_contain(term):
            return

        # 在Splunk中这可能是在O（log N）中N是terms的项数
        if term not in self.terms:
            return

        for event_id in sorted(self.terms[term]):
            yield self.events[event_id]

if __name__ == '__main__':
    s = Splunk()
    s.add_event('src_ip = 1234')
    s.add_event('src_ip = 5.6.7.8')
    s.add_event('dst_ip = 1.2.3.4')
    s.add_event(str(['华为','中兴','小米']))
    s.add_event('思科 华为 小米')
    s.add_event('华为 苹果 微软')

    for event in s.search('华为'):
        print (event)
    # print ('-')
    # for event in s.search('123'):
    #     print (event)
    # print ('-')
    # for event in s.search('src_ip'):
    #     print(event)
    # print('-')
    # for event in s.search('ip'):
    #     print (event)