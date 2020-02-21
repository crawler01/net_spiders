import requests
from lxml import etree
import random
import time


def towrite(content, title):
    with open('./wenzhang/' + title.replace('|', '').replace('?', '') + '.txt', 'wt', encoding='utf-8') as f:
        f.write(content)
        print('正在下载：', title)


def spider(url):
    hea = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
    proxies = [
        {'http': 'http://61.135.217.7:80'},
        {'https': 'https://59.62.49.106:45772'}
    ]
    r = requests.get(url, headers=hea)
    time.sleep(2)
    return etree.HTML(r.text)


def get_all_url(page_nums, keyword):
    for page_num in range(1, int(page_nums)+1):
        search_url = 'http://weixin.sogou.com/weixin?query=' + keyword + '&type=2&page=' + str(page_num) + '&ie=utf8'
        selector = spider(search_url)
        artical_urls = selector.xpath("//*[starts-with(@id,'sogou_vr_11002601_title_')]/@href")
        for artical_url in artical_urls:
            yield artical_url


def spider_xiangqing(url):
    selector = spider(url)
    title = selector.xpath('//h2[@class = "rich_media_title"]/text()')[0].strip()
    content = selector.xpath('string(//*[@class="rich_media_content "])').strip()
    towrite(content, title)


if __name__ == '__main__':
    keyword = input('请输入搜索内容：')
    page_num = input('请输入搜索页数（必须为自然数）:')
    for url in get_all_url(page_num, keyword):
        spider_xiangqing(url)