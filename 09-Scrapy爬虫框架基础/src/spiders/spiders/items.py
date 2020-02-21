# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BaiduItem(scrapy.Item):
    """
    创建百度爬虫需要采集的数据
    """
    title = scrapy.Field()
    url = scrapy.Field()
