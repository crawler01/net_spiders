# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['https://www.douban.com/']
    start_urls = ['http://https://www.douban.com//']

    def start_requests(self):
        return [scrapy.FormRequest('https://accounts.douban.com/passport/login',
                                   formdata={'username': '用户名', 'password': '密码'},
                                   callback=self.logged_in)]

    def logged_in(self,response):
        pass

    def parse(self, response):
        pass
