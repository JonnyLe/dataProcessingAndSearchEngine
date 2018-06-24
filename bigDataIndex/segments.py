# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-04-24'

# 下面一步我们要实现分词。 分词的目的是要把我们的文本数据分割成可搜索的最小单元，也就是词。
# 这里我们主要针对英语，因为中文的分词涉及到自然语言处理，比较复杂，而英文基本只要用标点符号就好了。
#实现分词，或者说是说是子字符串的提取
def major_segments(s):
    """
    在一个字符串上，一个大的分段。将所有主要的中断分割成字符串，并返回所找到的所有东西的集合。这个实现中的中断是单个字符，但是在Splunk中，它们可以是多个字符。
之所以使用set，是因为排序无关紧要，而重复是不好的
    """
    major_breaks = ' '
    last = -1
    results = set()

    # enumerate() will give us (0, s[0]), (1, s[1]), ...
    for idx, ch in enumerate(s):
        if ch in major_breaks:
            segment = s[last + 1:idx]
            results.add(segment)

            last = idx

    # 最后一个角色可能不是一个断点，所以总是捕捉
    # the last segment (which may end up being "", but yolo)
    segment = s[last + 1:]
    results.add(segment)

    return results


def minor_segments(s):
    """
   在一个字符串上执行一个小的分段。这就像一个大的分段，除了它也从每个中断的输入开始。
    """
    # minor_breaks = '_.'
    # ['临清', '恒中', '清园', '15', '烂尾楼', '聊城', '无望', '入住', '违约', '三百', '业主', '至此', '不管', '政府']
    minor_breaks = r"[' , ']"
    last = -1
    results = set()

    for idx, ch in enumerate(s):
        if ch in minor_breaks:
            segment = s[last + 1:idx]
            results.add(segment)
            segment = s[:idx]
            results.add(segment)
            last = idx
    segment = s[last + 1:]
    results.add(segment)
    results.add(s)

    return results


def segments(event):
  """简单的包装器关于 major_segments / minor_segments"""
  results = set()
  for major in major_segments(event):
    for minor in minor_segments(major):
      results.add(minor)
  return results

if __name__ == '__main__':
    # for term in segments('src_ip = 1.2.3.4/ha'):
    #     print (term)
    for term in segments(str(['临清','恒中','清园', '15', '烂尾楼', '聊城', '无望', '入住', '违约', '三百', '业主', '至此', '不管', '政府'])):
        print(term)