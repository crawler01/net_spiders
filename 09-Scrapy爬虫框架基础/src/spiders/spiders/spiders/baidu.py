# -*- coding: utf-8 -*-
import scrapy
from spiders.items import BaiduItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        item = BaiduItem()
        print('---------------------------')
        item['title'] = response.xpath('//*[@id="u1"]/a[1]/text()').extract()
        item['url'] = response.xpath('//*[@id="u1"]/a[1]/@href').extract_first()
        print(item['title'])
        print(item['url'])
        return item
