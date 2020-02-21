"""
在抽取列表页的基础上请求详情页数据
分析思路：
     1、 在列表页每个房源信息中抽取详情页链接
     2、 在抽取完成列表页数据完成后，发起requests请求收集详情页数据
     3、 xpath抽取目标数据
     4、 写文件保存数据
"""
import csv
import requests
from lxml import etree
import time

_base_url = "https://shenzhen.qfang.com"


def write_data(items):
    '''
    将爬取的房源信息写入到csv文件中
    :param items: 房源信息各种数据
    :return: None
    '''
    with open('houses_info.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(items)


def requests_url(url):
    '''
    根据url模拟headers请求，并将返回的html数据转换成文档对象，以便调用者拿到后直接用xpath抽取数据
    :param url:请求链接
    :return:返回HTML文档对象
    '''
    # 模拟浏览器头部信息
    # JSESSIONID=aaak70x19_-pHhNjYKY8w; acw_sc__v2=5e02f747de06403a1010f8ecbad144899fc40208;
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        'cookie': 'JSESSIONID=aaa0u1LqngmLc9oYVPY8w; acw_sc__v2=5e04092d3c54db59cb90dbb4b7c9e0c7939b8747; '
    }
    # 发起请求
    response = requests.get(url, headers=headers)
    # 将html字符串转换成文档对象
    return etree.HTML(response.text)


def spider(url):
    base_element = requests_url(url)
    # 利用xpath查找到当前页的所有房源信息
    houses_info = base_element.xpath('/html/body/div[5]/div/div[1]/div[4]/ul/li')
    # 循环遍历每套房源信息
    for house in houses_info:
        # 获取标题
        items = [house.xpath('div[2]/div[1]/a/text()')[0]]
        # 获取户型
        items.append(house.xpath('div[2]/div[2]/p[1]/text()')[0])
        # 获取面积
        items.append(house.xpath('div[2]/div[2]/p[2]/text()')[0])
        # 获取楼层
        items.append(house.xpath('div[2]/div[2]/p[4]/text()')[0])
        # 获取朝向
        items.append(house.xpath('div[2]/div[2]/p[5]/text()')[0])
        # 获取修建年限
        if house.xpath('div[2]/div[2]/p[6]/text()'):
            items.append(house.xpath('div[2]/div[2]/p[6]/text()')[0])
        # 获取代理房源中心
        if house.xpath('div[2]/div[3]/div/a[2]/text()'):
            items.append(house.xpath('div[2]/div[3]/div/a[2]/text()')[0])
        # 获取小区
        if house.xpath('div[2]/div[3]/div/a[3]/text()'):
            items.append(house.xpath('div[2]/div[3]/div/a[3]/text()')[0])
        # 获取价格
        items.append(house.xpath('string(div[3]/p[1])'))
        # 抽取详情页链接
        item_url = _base_url + house.xpath('div[1]/a/@href')[0]
        # 发起详情页链接请求
        items_element = requests_url(item_url)
        # 抽取数据  抵押时间和委托信息
        pledge = items_element.xpath('//*[@id="scrollto-1"]/div[2]/ul/li[2]/div/ul/li[5]/div/text()')[0]
        time_dis = items_element.xpath('//*[@id="scrollto-1"]/div[2]/ul/li[2]/div/ul/li[8]/div/text()')[0]
        items.append(pledge)
        items.append(time_dis)
        # 将爬取的数据写入csv文件
        write_data(items)


if __name__ == '__main__':
    for i in range(1, 2):
        spider(_base_url + "/sale/f" + str(i))
