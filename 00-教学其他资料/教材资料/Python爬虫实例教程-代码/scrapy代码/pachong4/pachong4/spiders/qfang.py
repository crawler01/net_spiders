# -*- coding: utf-8 -*-
import scrapy
from pachong4.items import Pachong4Item

class QfangSpider(scrapy.Spider):
    name = 'qfang'
    
    def start_requests(self):
        url_pre = 'http://m.qfang.com/shenzhen/sale?version=a&page='
        for i in range(1,6):
            url = url_pre +str(i)
            formdata = {'more':str(i)}
            yield scrapy.FormRequest(url,formdata = formdata,callback = self.parse)
    
    def parse(self, response):
        fang_list = response.xpath('//a')
        for fang in fang_list:
            item = Pachong4Item()
            item['mingcheng'] = fang.xpath('div[2]/p[1]/text()').extract()[0]
            item['jiage'] = fang.xpath('div[2]/p[3]/em/text()').extract()[0]
            yield item