# encoding=utf-8
__author__ = 'Jonny'
__location__ = '西安'
__date__ = '2018-04-24'

#架构一个网站，利用轻量级的tornato实现

from tornado import web,ioloop,httpserver
from bigDataIndex import dataHandle
from dataVis.quantityAnalysis import numberBarGraph,lineChart

class MainPageHandler(web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application=application,request=request)
        self.text = []
    def get(self,*args,**kwargs):
        self.render('index.html')
    def post(self,*args,**kwargs):
        # 从网页获取用户提交的数据
        text_temp = self.get_argument('text')
        #将用户数据传送到大数据搜索引擎中
        #将用户输入的关键词进行切割
        self.text = text_temp.split()
        # 将数据传送到数据库自带的搜索引擎中：
        # content = data.main(self.text)[1]
        #利用大叔数据搜索引擎实现数据处理
        content = dataHandle.main(self.text)[1]
        # 形成折线图，并存储
        lineChart.main(self.text)
        #形成统计图，并存储
        numberBarGraph.main(self.text)
        #加载网页
        self.render('result.html',content = content )

# 设置网站参数
setting = {
    # 设置模板路径
    'template_path':'template',
    'static_path':'static'
}
application = web.Application([
            (r"/index", MainPageHandler),
        ],**setting)

def main():
    http_server = httpserver.HTTPServer(application)
    http_server.listen(80)
    ioloop.IOLoop.current().start()


if __name__ =='__main__':
    main()

