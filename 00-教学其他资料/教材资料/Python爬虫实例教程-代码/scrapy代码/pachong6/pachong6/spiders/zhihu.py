# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pachong6.items import Pachong6Item
from scrapy.conf import settings

class ZhihuSpider(CrawlSpider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/kaifulee/activities']
    
    rules = (
        Rule(LinkExtractor(allow=(['people/.*/following$', 'people/.*/following?page']), )),
        Rule(LinkExtractor(allow=(['people/.*/followers$', 'people/.*/followers?page']), )),
        Rule(LinkExtractor(allow=('www.zhihu.com/people/((?!/).)*$', )), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = Pachong6Item()
        item['name'] = response.xpath("//*[@class='ProfileHeader-name']/text()").extract_first()
        item['intro'] = response.xpath("//*[@class='RichText ProfileHeader-headline']/text()").extract_first()
        item['detail'] = response.xpath("string(//*[@class='ProfileHeader-info'])").extract_first()
        item['following'] = response.xpath("//*[@class='NumberBoard-itemValue']/text()").extract()[0]
        item['followers'] = response.xpath("//*[@class='NumberBoard-itemValue']/text()").extract()[1]
        return item
