# -*- coding: utf-8 -*-
import re
import time

import scrapy
import requests
from spiders.items import LoveHomeItem


class LovehomeSpider(scrapy.Spider):
    name = 'lovehome'
    allowed_domains = ['bj.5i5j.com']
    # 创建需要采集列表页的页码数量
    start_urls = ['https://bj.5i5j.com/ershoufang/n' + str(page) for page in range(1, 2)]

    def parse(self, response):
        """
        创建采集过程中的采集业务逻辑，解析目标数据，其中对应的响应数据均在response中
        :param response: 对start_urls中的url请求后的响应返回对象
        :return:
        """
        if response.text.startswith('<HTML><HEAD><script>window.location.href'):
            # print(True)
            # print(re.search(r'https://.+\d+', response.text).group())
            real_url = re.search(r'https://.+\d+', response.text).group()
            yield scrapy.Request(real_url)
        # 提取每一页中的房源列表数据 //*[@class="pList"]/li
        page_list = response.xpath('/html/body/div[5]/div[1]/div[2]/ul/li')
        # print(response.text)
        for house in page_list:
            # 初始化目标采集项对象
            homeItem = LoveHomeItem()
            homeItem['title_name'] = house.xpath('div[2]/h3/a/text()').extract_first()
            homeItem['price'] = house.xpath('div[2]/div[1]/div/p[1]/strong/text()').extract_first()
            # print(homeItem['title_name'])
            # 解析并构建详情页URL
            house_url = response.urljoin(house.xpath('div[2]/h3/a/@href').extract_first())
            # 对house_url发起请求在详情页中获取经纪人姓名
            # 将返回的数据response传递给回调函数parse_detail，在parse_detail处理经纪人数据
            yield scrapy.Request(house_url, meta={'item': homeItem}, callback=self.parse_detail)

    def parse_detail(self, response):
        homeItem = response.meta['item']
        # 清洗过滤空数据 如果标题数据为空则不采集详情页
        if homeItem['title_name'] is None:
            return
        text = response.text
        """
        判断采集详情页是否有反爬如有返回内容为
        <HTML><HEAD><script>window.location.href='https://bj.5i5j.com/ershoufang/500455474.html?wscckey=cf7abd8dfcabb4c3_1581908669';</script></HEAD><BODY>
        如返回该内容从从抽取真实链接（用正则表达式），然后重新发起链接请求
        """
        if text.startswith('<HTML><HEAD><script>window.location.href'):
            real_url = re.search(r'https://.+\d+', text).group()
            yield scrapy.Request(real_url, meta={'item': homeItem}, callback=self.parse_detail)
        else:
            # 解析详情页中的经纪人数据
            homeItem['agent'] = response.xpath(
                '/html/body/div[4]/div[2]/div[2]/div[3]/ul/li[2]/h3/a/text()').extract_first()
            yield homeItem
