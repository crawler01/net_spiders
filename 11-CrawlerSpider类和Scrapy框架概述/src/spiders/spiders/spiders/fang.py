# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from spiders.items import FangItem


class FangSpider(CrawlSpider):
    name = 'fang'
    allowed_domains = ['cq.esf.fang.com']
    start_urls = ['https://cq.esf.fang.com/']

    """
        设置对应的rules规则
    """
    rules = (
        # Rule(LinkExtractor(allow=r'https://cq.esf.fang.com/house/i3.*')), # 采集整站数据
        Rule(LinkExtractor(allow=r'https://cq.esf.fang.com/house/i31'), follow=False),  # 测试时只采集第一页
        Rule(LinkExtractor(allow=r'https://cq.esf.fang.com/chushou/.*'), callback='parse_item'),
    )

    """
        解决在请求过程中的重定向问题，解决思路每次请求带上对应的header和cookies信息：
        参考网址：https://blog.csdn.net/godot06/article/details/81700310
        应对反爬虫针对重定向需要设置cookie，且在每次请求时均要带上该cookies和headers
    """
    headers = {
        'referer': 'https://cq.esf.fang.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }

    cookies = {'unique_cookie': 'U_vdw599fnazegjx9x0d8j6z0kk2dk6swy42k*60',
               'global_cookie': '64nj6jo7otdra03672hvunpgk17k6q5qtg4'}

    def _build_request(self, rule, link):
        """
        重写在除了第一次请求时设置header和cookies信息
        :param rule: 当前请求链接的rule对象
        :param link: 当前请求的链接信息对象
        :return:返回scrapy.Request对象交由队列处理
        """
        r = scrapy.Request(url=link.url, headers=self.headers, cookies=self.cookies, callback=self._response_downloaded)
        r.meta.update(rule=rule, link_text=link.text)
        return r

    def start_requests(self):
        """
        重写在第一次请求时设置header和cookies信息
        :return:返回scrapy.Request交给队列处理
        """
        yield scrapy.Request(url=self.start_urls[0],
                             headers=self.headers,
                             cookies=self.cookies,
                             callback=self.parse,
                             dont_filter=True)

    def parse_item(self, response):
        """
        针对详情页的解析业务逻辑
        :param response:详情页返回的response对象
        :return:返回item目标数据
        """
        item = FangItem()
        item['title'] = response.xpath('string(//*[@id="lpname"]/h1/span)').extract_first().strip()
        item['price'] = response.xpath('string(//*[@class="trl-item_top"]/div[1]/i)').extract_first().strip()
        item['area'] = response.xpath(
            'string(/html/body/div[4]/div[1]/div[4]/div[3]/div[2]/div[1])').extract_first().strip()
        return item
