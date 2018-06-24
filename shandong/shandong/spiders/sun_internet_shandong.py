# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from shandong.shandong.items import ShandongItem
import jieba
import jieba.analyse

class SunInternetShandongSpider(CrawlSpider):
    name = 'sun_internet_shandong'
    allowed_domains = ['minsheng.iqilu.com']
    start_urls = ['http://minsheng.iqilu.com/questions']

    rules = (
        Rule(LinkExtractor(allow=r'questions/index/page:\d+')),
        Rule(LinkExtractor(allow=r'/display/\d+')
             ,callback = 'parse_item',follow = False)
    )

    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        item = ShandongItem()
        item['title'] =''.join(response.xpath('/html/body/div[5]/div[2]/div[1]/div[1]/div/h2/text()').extract())
        item['target'] =''.join(response.xpath('/html/body/div[5]/div[2]/div[1]/div[2]/div/div[2]/div[1]/span/a/text()').extract())
        content = response.xpath('/html/body/div[5]/div[2]/div[1]/div[2]//div[2]/div[3]//text()').extract()
        content = ''.join(content).replace('\xa0','').replace('\u3000','').replace('\r','').replace('\n','')
        # if content == '' or '\xa0':
        #     content= response.xpath('/html/body/div[5]/div[2]/div[1]/div[2]//div[2]/div[3]///').extract()[0]
        item['reply'] = ''.join(response.xpath('/html/body/div[5]/div[2]/div[2]/div[2]//text()').extract()).replace('\n','')
        item['content'] = content
        item['keyword'] = jieba.analyse.extract_tags(content,30)
        date= ''.join(response.xpath('/html/body/div[5]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div//text()').extract()).split(' ')
        item['date'] = date[-2]+' '+date[-1]
        yield item
