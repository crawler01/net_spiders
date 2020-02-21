"""
需求：采集链家移动端经纪人信息
分析：
    1.分析链接，链家经纪人会根据页面下拉发起新的链接请求，分析链接
    2.根据需求构建对应的请求url链接地址
    3.发起请求返回数据并解析
    4.写入文件

实现：
    1.定义一个函数实现将列表数据写入csv文件
    2.定一个函数接收链接地址并返回json对象
    3.定义一个函数发起请求解析得到的数据并调用1中的函数写入文件
"""

import csv
import requests
from lxml import etree


def write_data(items):
    """
    实现将列表数据写入csv文件
    :param items:列表数据
    :return:将内容写入文件无返回值
    """
    with open("lianjia_workers.csv", "a", encoding='gbk', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(items)


def spider(url):
    """
    给目标url地址requests请求，将返回的内容用etree处理
    :param url: 目标url资源地址
    :return: 返回json对象
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.json()


def get_agents(pages):
    """
    传入需要采集的经纪人人数
    根据人数构建链接地址
    发起requests请求解析数据
    写入文件
    地址格式：
    :param pages: 需要采集的页码经纪人
    :return: 解析数据写入文件
    """
    home_url = "https://m.lianjia.com/liverpool/api/jingjiren/getList?cityId=500000&condition=%252Fao22pg"
    for page in range(1, pages + 1):
        json_data = spider(home_url + str(page))
        agents_info = json_data['data']['data']['getJingJiRenList']['list']
        for agent in agents_info:
            agent_info = [agent['name'], agent['storeName'], ",".join(agent['tags'])]
            for item in agent['statistics']:
                agent_info.append(item['category'] + item['datum'])
            write_data(agent_info)


if __name__ == '__main__':
    get_agents(5)
