# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-03-24'

from scrapy import cmdline
def start():
    cmdline.execute('scrapy crawl sun_internet_shandong'.split())


if __name__ == '__main__':
    start()