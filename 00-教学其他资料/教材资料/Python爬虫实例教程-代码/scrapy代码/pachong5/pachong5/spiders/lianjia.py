# -*- coding: utf-8 -*-
import scrapy
from pachong5.items import Pachong5Item


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = (
        'https://m.lianjia.com/bj/jingjiren?page_size=15&t=1&offset=' + str(x) for x in range(0,30,15)
                 )
    def parse(self, response):
        jjrlist = response.xpath("//*[@class='lists q_agentlist']/li[@class = 'pictext flexbox box_center_v']")
        for jjr in jjrlist:
            item=Pachong5Item()
            item['xingming'] = jjr.xpath('div[2]/div[1]/span[1]/a/text()').extract_first()
            item['bankuai'] = jjr.xpath('div[2]/div[2]/span[1]/text()').extract_first()
            xiangqing_url = 'https://m.lianjia.com/bj/jingjiren/chengjiao/' + jjr.xpath('div[2]/div[1]/span[1]/a/@href').extract_first().split('/')[-2] + '?page_size=20&_t=1&offset=0'
            yield scrapy.Request(url = xiangqing_url, meta={'item':item},callback = self.parse_xiangqing)
            
    def parse_xiangqing(self, response):
        chengjiaos=response.xpath("//*[@class='mod_cont']/ul/li[@class='pictext']")
        if chengjiaos:
            item=response.meta['item']
            next_url = response.url.rsplit('=',1)[0] + '=' + str(int(response.url.rsplit('=',1)[1]) + 20)
            yield scrapy.Request(url = next_url, meta={'item':item},callback = self.parse_xiangqing)
            for chengjiao in chengjiaos:
                item['cjxiaoqu']=chengjiao.xpath('a/div[2]/div[1]/text()').extract_first()         
                item['cjshijian']=chengjiao.xpath('a/div[2]/div[3]/text()').extract_first()           
                item['cjzongjia']=chengjiao.xpath('a/div[2]/div[4]/span[1]/em/text()').extract_first()
                yield item
            