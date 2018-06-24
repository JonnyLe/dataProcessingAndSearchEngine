# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShandongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    target = scrapy.Field()
    content = scrapy.Field()
    reply = scrapy.Field()
    date = scrapy.Field()
    keyword = scrapy.Field()
