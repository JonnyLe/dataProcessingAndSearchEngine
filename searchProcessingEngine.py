# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-04-26'

#本文件用于整个各个子程序，确保程序的正常运行，
#对于和网页数据的交互采取两种方式，一种方式时利用“伪服务器”，另一种方式就是利用多线程实现，初步打算利用线程实现


from shandong.shandong import start
from dataVis.webUI import data_web_ui


#程序运行的第一步，需要先将数据进行入库：
def main():
    #运行数据库，实现数据的采集和存储
    start.start()
    # 运行网页客户端程序
    data_web_ui.main()


if __name__ == '__main__':
    main()

