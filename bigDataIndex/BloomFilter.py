# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-04-23'

# 第一步我们先要实现一个布隆过滤器。

# 布隆过滤器是大数据领域的一个常见算法，它的目的是过滤掉那些不是目标的元素。也就是说如果一个要搜索的词并不存在与我的数据中，
# 那么它可以以很快的速度返回目标不存在。
# 基本的数据结构是个数组（实际上是个位图，用1/0来记录数据是否存在），初始化是没有任何内容，所以全部置False。实际的使用当中，该数组的长度是非常大的，以保证效率。
# 利用哈希算法来决定数据应该存在哪一位，也就是数组的索引
# 当一个数据被加入到布隆过滤器的时候，计算它的哈希值然后把相应的位置为True
# 当检查一个数据是否已经存在或者说被索引过的时候，只要检查对应的哈希值所在的位的True／Fasle
# 看到这里，大家应该可以看出，如果布隆过滤器返回False，那么数据一定是没有索引过的，然而如果返回True，那也不能说数据一定就已经被索引过。
# 在搜索过程中使用布隆过滤器可以使得很多没有命中的搜索提前返回来提高效率。


class bloomfilter(object):

    def __init__(self, size):
        """设置具有适当大小的BF"""
        self.values = [False] * size
        self.size = size

    def hash_value(self, value):
        """对所提供的值进行散列，并将其缩放以适应BF大小"""
        return hash(value) % self.size

    def add_value(self, value):
        """添加一个值到BF"""
        h = self.hash_value(value)
        self.values[h] = True

    def might_contain(self, value):
        """检查这个值是否在BF中"""
        h = self.hash_value(value)
        return self.values[h]

    def print_contents(self):
        """为了调试目的，转储BF的内容"""
        print (self.values)


#测试用例：
if __name__ == '__main__':
    bf = bloomfilter(10)
    bf.add_value('dog')
    bf.add_value('fish')
    bf.add_value('cat')
    # bf.print_contents()
    bf.add_value('bird')
    # bf.print_contents()
    # Note: contents are unchanged after adding bird - it collides
    for term in ['dog', 'fish', 'cat', 'bird', 'duck', 'emu']:
        print('{}: {} {}'.format(term, bf.hash_value(term), bf.might_contain(term)))
