# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Pachong6Item(scrapy.Item):
    name = scrapy.Field()
    intro = scrapy.Field()
    detail = scrapy.Field()
    following = scrapy.Field()
    followers = scrapy.Field()