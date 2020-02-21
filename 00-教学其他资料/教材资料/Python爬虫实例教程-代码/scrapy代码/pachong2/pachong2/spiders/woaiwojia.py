# -*- coding: utf-8 -*-
import scrapy
from pachong2.items import Pachong2Item

class WoaiwojiaSpider(scrapy.Spider):
    name = 'woaiwojia'
    allowed_domains = ['bj.5i5j.com']
    start_urls = ['https://bj.5i5j.com/ershoufang/']

    def parse(self, response):
        house_list = response.xpath('//*[@class="pList"]/li')
        for house in house_list:
            item = Pachong2Item()
            item['xiaoqu'] = house.xpath('div[2]/h3/a/text()').extract_first()
            item['zongjia'] = house.xpath('div[2]/div[1]/div/p[1]/strong/text()').extract_first()
            url = response.urljoin(house.xpath('div[2]/h3/a/@href').extract_first())
            yield scrapy.Request(url,meta = {'item':item},callback = self.parse_detail)
        next_url = response.xpath('//div[@class="pageSty rf"]/a[1]/@href').extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url,callback = self.parse)
    def parse_detail(self, response):
        item = response.meta['item']
        item['jingjiren'] = response.xpath('//*[@class="daikansty"]/ul/li[2]/h3/a/text()').extract_first()
        yield item
