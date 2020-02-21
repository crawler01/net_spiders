# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pachong4.items import Pachong4Item


class FangSpider(CrawlSpider):
    name = 'fang'
    allowed_domains = ['fang.com']
    start_urls = ['http://esf.fang.com/']

    rules = (
        Rule(LinkExtractor(allow='http://esf.fang.com/house.*')),
        Rule(LinkExtractor(allow='http://esf.fang.com/chushou/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = Pachong4Item()
        item['xiaoqu'] = response.xpath('string(//div[@class="tab-cont clearfix"]/div[1])').extract_first().strip().split('\r\n')[0].strip()
        item['zongjia'] = response.xpath('//div[@class="trl-item_top"]/div[1]/i/text()').extract_first()
        item['mianji'] = response.xpath('//div[@class="tt"]/text()').extract()[1]
        return item
