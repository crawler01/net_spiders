import requests
from lxml import etree
import csv
from multiprocessing.dummy import Pool as pl

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
pre_url = 'http://shenzhen.qfang.com/sale/f'

def download(url):
    html = requests.get(url, headers=headers)
    return etree.HTML(html.text)

def csv_writer(item):
    with open('qfang_ershoufang.csv', 'a',encoding='utf-8',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(item)

def spider(url):
    selector = download(url)
    house_list = selector.xpath("//*[@id='cycleListings']/ul/li")
    for house in house_list:
        xiaoqu = house.xpath("div[1]/p[1]/a/text()")[0]
        huxing = house.xpath("div[1]/p[2]/span[2]/text()")[0]
        mianji = house.xpath("div[1]/p[2]/span[4]/text()")[0]
        quyu = house.xpath("div[1]/p[3]/span[2]/a[1]/text()")[0]
        zongjia = house.xpath("div[2]/span[1]/text()")[0]
        house_url = 'http://shenzhen.qfang.com' + house.xpath("div[1]/p[1]/a/@href")[0]
        sel = download(house_url)
        time.sleep(1)
        nianxian = sel.xpath("//div[@class='housing-info']/ul/li[2]/div/ul/li[3]/div/text()")[0]
        diya_info = sel.xpath("//div[@class='housing-info']/ul/li[2]/div/ul/li[5]/div/text()")[0]
        item = [xiaoqu, huxing, mianji, quyu, zongjia, nianxian, diya_info]
        print('正在抓取', xiaoqu)
        csv_writer(item)
        image_url = house.xpath('a/img/@data-original')[0]
        img = requests.get(image_url, headers=headers)
        with open('./Qfang_image/{}.jpg'.format(xiaoqu), 'wb') as f:
            f.write(img.content)

if  __name__ == '__main__':
    for x in range(1,11):
        spider(pre_url + str(x))