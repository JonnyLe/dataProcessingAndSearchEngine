# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-04-22'
#定性分析，绘制柱状图


from matplotlib import pyplot
from dataVis import data


#绘制柱状图
def drawBar(grades):
    # xticks = ['0~4', '4~8', '8~12', '12~16', '16~20','20~24']
    xticks = ['0~60', '60~75', '75~80', '80~90', '90~100']
    gradeGroup = {}
    #对每一类成绩进行频数统计
    for grade in grades:
        gradeGroup[grade] = gradeGroup.get(grade, 0) + 1

    print(gradeGroup)
    #创建柱状图
    #第一个参数为柱的横坐标
    #第二个参数为柱的高度
    #参数align为柱的对齐方式，以第一个参数为参考标准
    # pyplot.bar(range(6), [gradeGroup.get(xtick, 0) for xtick in xticks], align='center')
    #设置柱的文字说明
    #第一个参数为文字说明的横坐标
    #第二个参数为文字说明的内容
    pyplot.xticks(range(6), xticks)

    #设置横坐标的文字说明
    pyplot.xlabel('Time')
    #设置纵坐标的文字说明
    pyplot.ylabel('Frequency')
    #设置标题
    pyplot.title('keyword display')
    #绘图
    pyplot.show()

if __name__ == '__main__':
    grades = [12,34,56,87,83,23,35,56,6,89,87,89,78,67,56,77,90,97,96,87,67,89,67,89,67,78,98,97,97,98]
    drawBar(grades)