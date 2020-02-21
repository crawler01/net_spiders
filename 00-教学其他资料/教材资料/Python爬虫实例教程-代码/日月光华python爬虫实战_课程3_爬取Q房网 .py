#-*- coding:utf-8 -*-
from lxml import etree
import requests
import csv
import time

def towrite(item):
    with open('qfang_xiaoqu1.csv', 'a',encoding='utf-8',newline='') as csvfile:
        writer = csv.writer(csvfile)
        try:
            writer.writerow(item)
        except:
            print('write error!')
        finally:
            return


if  __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
    start_url = 'http://beijing.qfang.com/garden/n'
    xx = 1
    for x in range(1,5):
        html = requests.get(start_url + str(x), headers=headers)
        time.sleep(1)
        slector = etree.HTML(html.text)
        xiaoqulist = slector.xpath("//*[@id='cycleListings']/ul/li")
        for xiaoqu in xiaoqulist:
            xiaoqumingcheng = xiaoqu.xpath("div[1]/p[1]/a/text()")[0]
            bankuai = xiaoqu.xpath("div[1]/p[3]/span[1]/text()")[0]
            xiaoqujiage = xiaoqu.xpath("div[2]/p[1]/span[1]/text()")[0]
            xiaoqu_item = [xiaoqumingcheng,bankuai,xiaoqujiage]
            towrite(xiaoqu_item)
            print('正在抓取小区：',xiaoqumingcheng)
