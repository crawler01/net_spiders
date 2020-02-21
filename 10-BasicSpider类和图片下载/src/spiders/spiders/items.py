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


class LoveHomeItem(scrapy.Item):
    """
    创建我爱我家采集目标项数据类
    """
    title_name = scrapy.Field()  # 房源标题
    price = scrapy.Field()  # 房源价格
    agent = scrapy.Field()  # 房源经纪人

    # 添加采集图片字段
    image_urls = scrapy.Field()  # 图片地址
    images = scrapy.Field()  # 图片
