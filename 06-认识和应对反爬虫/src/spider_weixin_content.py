"""
需求：使用代理ip采集微信文章内容
分析：
    1.分析微信文章搜索url链接
    2.根据url链接的规律找到对应关键字对应页码的列表页所有文章url地址
    3.根据url地址采集对应的标题和内容
    4.将采集的内容写入磁盘中
实现：
    1.函数一 编写一个函数将内容写入硬盘文件中
    2.函数二 编写一个函数接收url地址采用临时代理ip发起请求返回etree处理后的对象
    3.函数三 编写一个函数接收搜索关键字和页码值返回列表页所有url地址
    4.函数四 编写一个函数解析文章详细内容，将得到的内容传给函数一写入文件
"""

import requests
import random
from lxml import etree


def write_data(title, content):
    """
    传入文章标题和文章内容将内容写入到文件中  wt t指的是Windows平台下的文本模式
    :param title: 文章标题
    :param content: 文章内容
    :return: 无返回值
    """
    with open('./articles/' + title.replace('|', '').replace('?', '') + '.txt', 'wt', encoding='utf-8') as file:
        file.write(content)


def spider(url):
    """
    给目标url地址利用代理ip发起requests请求，将返回的内容用etree处理
    :param url: 目标url资源地址
    :return: 返回etree处理后的文档对象
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }
    proxies = [
        {"http": "https://183.151.41.148:3128"},
        {"http": "http://175.44.109.194:9999"},
        {"http": "http://114.99.25.98:18118"}
    ]
    response = requests.get(url, headers=headers, proxies=random.choice(proxies))
    print(response.text)
    return etree.HTML(response.text)


def get_all_url(page_num, keyword):
    """
    根据页码值和搜索关键字获取对应列表页的所有文章的url地址链接
    :param page_num: 页码
    :param keyword: 搜索关键字
    :return: 返回所有URL地址
    """
    for page in range(1, page_num + 1):
        key_url = "https://weixin.sogou.com/weixin?query=" + keyword + '&type=2&page=' + str(page) + '&ie=utf8'
        elements = spider(key_url)
        article_urls = elements.xpath("//*[starts-with(@id,'sogou_vr_11002601_title_')]/@href")
        return article_urls


def parse_item(item_url):
    """

    解析对应url文章的内容
    :param item_url: 文章url
    :return: 无返回值
    """
    article_element = spider(item_url)
    title = article_element.xpath('//*[@id="activity-name"]/text()')[0].strip()
    print(title)
    content = article_element.xpath('string(//*[@id="js_content"])').strip()
    print(content)
    write_data(title, content)


if __name__ == '__main__':
    item_url = "https://mp.weixin.qq.com/s?src=11&timestamp=1580873348&ver=2139&signature=Ydb9FXbmFeN-XMAo6fgczXLt6xsrhqHX2*Sm*y8fgjVOM-*MZDmwJODW*4GErJvHrZ26CymgKAqdXFOZQA3i8VdEERaEfo9WfE1fj*zWC9rx*S9QZ9ADErRScRGskkKI&new=1"
    urls = get_all_url(1, "python")
    parse_item(item_url)
