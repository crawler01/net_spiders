# -*- coding: utf-8 -*-
import scrapy
from pachong1.items import Pachong1Item

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        item = Pachong1Item()
        item['title'] = response.selector.xpath('//*[@id="u1"]/a[1]/text()').extract()[0]
        item['url'] = response.selector.xpath('//*[@id="u1"]/a[1]/@href').extract()[0]
        print(item['title'])
        print(item['url'])
        return item
