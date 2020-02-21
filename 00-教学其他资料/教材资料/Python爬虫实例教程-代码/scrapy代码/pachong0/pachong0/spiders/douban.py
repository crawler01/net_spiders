# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/accounts/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'source':'index_nav','form_email':'984595060@qq.com','form_password':'root123'},
            callback=self.after_login)
    def after_login(self, response):
        zuozhe = response.xpath('//*[@id="statuses"]/div[2]/div[1]/div/div/div[1]/div[2]/a/text()').extract_first()
        print(zuozhe)
        with open('db.txt','wb') as f:
            f.write(response.body)
        return
