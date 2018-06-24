# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-04-22'

from matplotlib import pyplot
from dataVis import data
import collections
from bigDataIndex import dataHandle

# 控制图片显示中文
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


def autoLabel(rects):
    for rect in rects:
        height = rect.get_height()
        pyplot.text(rect.get_x()+rect.get_width()/4, 1.03*height, '%s' % int(height))


#绘制直方图
def drawHist(data):
    xticks = ['0~4', '4~8', '8~12', '12~16', '16~20', '20~24']
    total_width, n = 0.8, 4
    width = total_width / n
    d = {}
    label =[]
    x = list(range(6))
    color = ['b','g','r','y']
    i = 0
    print(data)
    for k in data:
        d = collections.Counter(data[k])
        print(d)
        keyword1 = pyplot.bar(x, [d.get(xtick, 0) for xtick in xticks], width=width, label =k , fc=color[i])
        autoLabel(keyword1)
        i += 1
        for j in range(len(x)):
            x[j] = x[j] + width
    #创建直方图
    #第一个参数为待绘制的定量数据，不同于定性数据，这里并没有事先进行频数统计
    #第二个参数为划分的区间个数
    pyplot.xticks(range(6), xticks)
    pyplot.xlabel('Time（H）')
    pyplot.ylabel('Amount(条/2h)')
    pyplot.title('Sum Of Keyword')
    pyplot.grid(True)
    pyplot.legend()
    pyplot.savefig(r"E:\Python\dataProcessingAndSearchEngine\dataVis\webUI\static\bower_components\bootstrap\dist\img\numBar.jpg")
    # pyplot.show()
    plt.close()

def main(keyword):
    # print(data.main())
    #通过数据直接绘制数据库
    # drawHist(data.main(keyword)[0])
    #通过数据索引查找数据
    drawHist(dataHandle.main(keyword)[0])


if __name__=='__main__':
    main(['济南','潍坊','淄博'])