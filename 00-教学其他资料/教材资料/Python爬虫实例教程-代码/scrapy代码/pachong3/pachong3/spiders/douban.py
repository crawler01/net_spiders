# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    
    cookies = {'__yadk_uid': 'uwFVPJdkcfceabbhFWVvr7vsn5bYMoE7',
 '_pk_id.100001.8cb4': 'c4c3300346e5c286.1520861244.1.1520861578.1520861244.',
 '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1520861244%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DWtNOI1ojokVsXT3LiWmCRh16WD0TkGuk5AK2wjO484OzHFMoc8YfiZ-Hdk9RSTnp%26wd%3D%26eqid%3Da343542800001769000000035aa68036%22%5D',
 '_pk_ses.100001.8cb4': '*',
 'bid': 'gv3lmrowlGU',
 'ck': 'To-U',
 'dbcl2': '165023527:i0lDyRKYNTU',
 'll': '108288',
 'ps': 'y',
 'ue': '984595060@qq.com'}

    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'www.douban.com',
        'Upgrade-Insecure-Requests':'1',
        'Referer':'https://www.douban.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
        
    def start_requests(self):
        url = 'https://www.douban.com/people/xpython/'
        yield scrapy.Request(url,cookies = self.cookies,headers = self.headers,callback = self.parse)
    
    def parse(self, response):
        name = response.xpath('//*[@id="db-usr-profile"]/div[1]/a/img/@alt').extract_first()
        print(name)
        url_shouye = 'https://www.douban.com/'
        yield scrapy.Request(url_shouye,cookies = self.cookies,headers = self.headers,callback = self.parse_shouye)
        
    def parse_shouye(self, response):
        zuozhe = response.xpath('//*[@id="statuses"]/div[2]/div[1]/div/div/div[1]/div[2]/a/text()').extract_first()
        print(zuozhe)
