# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pachong3.items import Pachong3Item
from scrapy_redis.spiders import RedisCrawlSpider


class LianjiaSpider(RedisCrawlSpider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    redis_key = 'LianjiaSpider:start_urls'
	
    rules = (
        Rule(LinkExtractor(allow=(r'ershoufang/',))),
        Rule(LinkExtractor(allow=('\d{12}\.html',)), callback='parse_detail'),
    )

    def parse_detail(self, response):
        item = Pachong3Item()
#        from scrapy.shell import inspect_response
#        inspect_response(response, self)
        item['xiaoqu'] = response.xpath('//div[@class="communityName"]/a[1]/text()').extract_first()
        item['zongjia'] = response.xpath('//div[@class="price "]/span/text()').extract_first()
        item['danjia'] = response.xpath('//span[@class="unitPriceValue"]/text()').extract_first()
        return item