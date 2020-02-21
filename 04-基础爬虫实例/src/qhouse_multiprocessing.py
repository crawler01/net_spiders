"""
在详情页数据采集基础上完成以下两个功能：
1.采集列表页标题图片 以小区+时间戳命名
2.多线程下载
"""
import csv
import requests
from lxml import etree
import time
from multiprocessing.dummy import Pool as pl
from multiprocessing.pool import ThreadPool as p

_base_url = "https://shenzhen.qfang.com"
# 模拟浏览器头部信息 JSESSIONID=aaak70x19_-pHhNjYKY8w; acw_sc__v2=5e041c4283a1b534bda185141975a042a29edca7;
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    'cookie': 'JSESSIONID=aaa0u1LqngmLc9oYVPY8w; acw_sc__v2=5e0428dab12cf72044969a985085457d8d2e9925; '
}


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
    # 发起请求
    response = requests.get(url, headers=headers)
    # 将html字符串转换成文档对象
    return etree.HTML(response.text)


def request_save_img(department, img_url):
    '''
    根据图片地址下载图片到本地
    :param department:小区名字
    :param img_url:图片网络地址
    :return:None
    '''
    response = requests.get(img_url, headers=headers)
    with open('./imgs/{}.jpg'.format(department + "_" + str(time.time())), 'wb') as f:
        f.write(response.content)


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
        department = ""
        if house.xpath('div[2]/div[3]/div/a[3]/text()'):
            department = house.xpath('div[2]/div[3]/div/a[3]/text()')[0]
            items.append(department)
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

        # 抽取列表页标题图片
        # 获取图片地址
        img_url = house.xpath('div[1]/a/img/@data-original')[0]
        request_save_img(department, img_url)
        # 将爬取的数据写入csv文件
        write_data(items)


if __name__ == '__main__':
    # 创建初始化一个连接池
    pool = pl(4) # type:p
    # 构建列表页地址
    house_url = [_base_url + "/sale/f" + str(i) for i in range(1, 5)]
    # 向连接池加入任务
    pool.map(spider, house_url)
    # 关闭线程池等待线程执行完毕
    pool.close()
    pool.join()
