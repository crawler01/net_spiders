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


class FangItem(scrapy.Item):
    """
    需要采集的目标数据项内容
    """
    title = scrapy.Field()  # 房源标题
    price = scrapy.Field()  # 房源价格
    area = scrapy.Field()  # 房源面积
