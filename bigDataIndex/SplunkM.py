# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-04-24'

# 更复杂的搜索
# 更进一步，在搜索过程中，我们想用And和Or来实现更复杂的搜索逻辑。
# 利用Python集合的intersection和union操作，可以很方便的支持And（求交集）和Or（求合集）的操作

from bigDataIndex import BloomFilter
from bigDataIndex import segments


class SplunkM(object):
    def __init__(self):
        self.bf = BloomFilter.bloomfilter(64)
        self.terms = {}  # 存放时间集合的字典集
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

    def search_all(self, terms):
        """搜索所有的术语"""

        # Start with the universe of all events...
        results = set(range(len(self.events)))

        for term in terms:
            # If a term isn't present at all then we can stop looking
            if not self.bf.might_contain(term):
                return
            if term not in self.terms:
                return

            # Drop events that don't match from our results
            results = results.intersection(self.terms[term])

        for event_id in sorted(results):
            yield self.events[event_id]

    def search_any(self, terms):
        """Search for an OR of all terms"""
        results = set()

        for term in terms:
            # If a term isn't present, we skip it, but don't stop
            if not self.bf.might_contain(term):
                continue
            if term not in self.terms:
                continue

            # Add these events to our results
            results = results.union(self.terms[term])

        for event_id in sorted(results):
            yield self.events[event_id]


if __name__ == '__main__':
    s = SplunkM()
    s.add_event('src_ip = 1.2.3.4')
    s.add_event('src_ip = 5.6.7.8')
    s.add_event('dst_ip = 1.2.3.4')
    s.add_event('华为 思科 思念 中华')
    s.add_event('华为 中华')
    print('华为 思科 思念 中华' in (s.search_all('华为 思科 思念 中华')))
    for event in s.search_all(['华为']):
        print (event)
    print ('-')
    for event in s.search_all(['src_ip', '5.6']):
        print (event)
    print ('-')
    print('src_ip = 1.2.3.4' in s.search_any(['src_ip', 'dst_ip']))
    for event in s.search_any(['src_ip', 'dst_ip']):
        print (event)