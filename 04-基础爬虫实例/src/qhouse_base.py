"""
任务描述：爬取Q房网二手房前10页的房源信息
Q房网url：https://shenzhen.qfang.com
分析分页链接：https://shenzhen.qfang.com/sale/f1
            f1中的1代表页码，f1-f10
分析思路：
        1.分析链接
        2.获取单页中的所有房源信息
        3.循环每套房源的细节信息
        4.保存信息
"""
import csv
import requests
from lxml import etree
import time


def write_data(items):
    '''
    将爬取的房源信息写入到csv文件中
    :param items: 房源信息各种数据
    :return: None
    '''
    with open('houses_info.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(items)


def spider():
    # 模拟浏览器头部信息
    # JSESSIONID=aaak70x19_-pHhNjYKY8w; acw_sc__v2=5e02f747de06403a1010f8ecbad144899fc40208;
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        'cookie': 'JSESSIONID=aaak70x19_-pHhNjYKY8w; acw_sc__v2=5e02f747de06403a1010f8ecbad144899fc402081; '
    }
    # 基础链接
    base_url = "https://shenzhen.qfang.com/sale/f"
    for i in range(1, 2):
        # 构建url链接发起请求
        response = requests.get(base_url + str(i), headers=headers)
        print(response.text)
        # 睡眠3秒再次发起请求
        time.sleep(3)
        # 将html字符串转换成文档对象
        base_element = etree.HTML(response.text)
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
            items.append(house.xpath('div[2]/div[2]/p[6]/text()')[0])
            # 获取代理房源中心
            if house.xpath('div[2]/div[3]/div/a[2]/text()'):
                items.append(house.xpath('div[2]/div[3]/div/a[2]/text()')[0])
            # 获取小区
            if house.xpath('div[2]/div[3]/div/a[3]/text()'):
                items.append(house.xpath('div[2]/div[3]/div/a[3]/text()')[0])
            # 获取价格
            items.append(house.xpath('string(div[3]/p[1])'))
            # 将爬取的数据写入csv文件
            write_data(items)


if __name__ == '__main__':
    spider()
