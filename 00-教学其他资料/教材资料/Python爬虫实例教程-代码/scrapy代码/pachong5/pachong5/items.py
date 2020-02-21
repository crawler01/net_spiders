# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Pachong5Item(scrapy.Item):
    xingming = scrapy.Field()
    bankuai = scrapy.Field()
    cjxiaoqu = scrapy.Field()
    cjshijian = scrapy.Field()
    cjzongjia = scrapy.Field()
