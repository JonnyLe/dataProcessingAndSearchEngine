# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-05-08'


import matplotlib.pyplot as plt
from bigDataIndex import dataHandle
import collections
from pylab import *  # 支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']


def line_chart(keyDict):

    xticks = ['0~4', '4~8', '8~12', '12~16', '16~20', '20~24']
    marker = ['o','*','v','x']
    colors =['r','g','b','c','m','y']
    x = range(len(xticks))

    # plt.plot(x, y, 'ro-')
    # plt.plot(x, y1, 'bo-')
    # plt.xlim(-1, 11)  # 限定横轴的范围
    plt.ylim(-1, 50)  # 限定纵轴的范围
    i = 0
    ax = plt.gca()
    for k in keyDict:
        d = collections.Counter(keyDict[k])
        y = [d.get(xtick, 0) for xtick in xticks]
        print('y:' + str(y))
        plt.plot(x,y,marker = marker[i%4],mec=colors[i%6],mfc = 'w' ,label = k)
        for x0,y0 in zip(x,y):
            ax.text(x0,y0,str(y0),color=colors[i%6],fontsize = 12)
        i += 1
    plt.legend(loc = 2)  # 让图例生效
    plt.xticks(x, xticks, rotation=45)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"time(H)")  # X轴标签
    plt.ylabel("Amount(条/2h)")  # Y轴标签
    plt.title("Sum Of Keyword")  # 标题
    plt.savefig(r"E:\Python\dataProcessingAndSearchEngine\dataVis\webUI\static\bower_components\bootstrap\dist\img\lineChart.jpg")
    # plt.show()
    plt.close()


def main(keyword):
    line_chart(dataHandle.main(keyword)[0])


if __name__ == '__main__':
    keyword = ['济南','淄博']
    main(keyword)