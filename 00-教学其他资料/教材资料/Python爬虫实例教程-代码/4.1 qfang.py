from lxml import etree
import requests
import csv
import time

def data_writer(item):
    with open('qfang_ershoufang.csv', 'a',encoding='utf-8',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(item)
def spider():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
    pre_url = 'http://shenzhen.qfang.com/sale/f'
    for x in range(1,11):
        html = requests.get(pre_url + str(x), headers=headers)
        time.sleep(2)
        selector = etree.HTML(html.text)
        house_list = selector.xpath("//*[@id='cycleListings']/ul/li")
        for house in house_list:
            xiaoqu = house.xpath("div[1]/p[1]/a/text()")[0]
            huxing = house.xpath("div[1]/p[2]/span[2]/text()")[0]
            mianji = house.xpath("div[1]/p[2]/span[4]/text()")[0]
            quyu = house.xpath("div[1]/p[3]/span[2]/a[1]/text()")[0]
            zongjia = house.xpath("div[2]/span[1]/text()")[0]
            item = [xiaoqu, huxing, mianji, quyu, zongjia]
            data_writer(item)
            print('正在抓取', xiaoqu)

if __name__ == '__main__':
    spider()