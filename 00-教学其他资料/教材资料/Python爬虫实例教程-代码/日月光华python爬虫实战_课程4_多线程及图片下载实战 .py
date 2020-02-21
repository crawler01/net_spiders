#-*- coding:utf-8 -*-
from lxml import etree
import requests
import csv
from multiprocessing.dummy import Pool as pl     #导入线程池

def towrite(item):
    with open('qfang_xiaoqu.csv', 'a',encoding = 'utf-8') as csvfile:
        writer = csv.writer(csvfile)
        try:
            writer.writerow(item)
        except:
            print('write error!')
            
def spider(url):
    htm = requests.get(url, headers=headers)
    response=etree.HTML(htm.text)
    xiaoqumingcheng = response.xpath('/html/body/div[3]/h2/text()')[0]
    bankuai = response.xpath('/html/body/div[4]/text()')[0]
    jiage = response.xpath('//*[@id="headInfo"]/div/div[2]/div[1]/span')[0]
    wuye = response.xpath("//*[@id='headInfo']/div/div[2]/div[3]/ul/li[7]/p/text()")[0]
    wuyefei = wuye.split('/')[0]
    xiaoqu_item = [xiaoqumingcheng,bankuai,jiage,wuyefei]
    towrite(xiaoqu_item)
    print('正在爬取小区：',xiaoqumingcheng)
    tupian_url = response.xpath("//*[@id='previewCon']/img/@src")[0]
    b_tupian = requests.get(tupian_url, headers=headers)
    with open('./xiaoqutupian/' + xiaoqumingcheng + '.jpg','wb') as tp:
        tp.write(b_tupian.content)
        print('正在下载图片：', xiaoqumingcheng)


if  __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
    all_url = ['http://m.lagou.com/search.json?city=%E5%85%A8%E5%9B%BD&positionName=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&pageNo=' + str(x) + '&pageSize=15' for x in range(1,5)]
    pool=pl(4)
    all_url = []
    for x in range(1,5):
        html = requests.get(start_url + str(x), headers=headers)
        slector = etree.HTML(html.text)
        xiaoqulist = slector.xpath("//*[@id='cycleListings']/ul/li")
        for xiaoqu in xiaoqulist:
            xiaoqu_url_houduan = xiaoqu.xpath("div[1]/p[1]/a/@href")[0]
            xiaoqu_url = 'http://beijing.qfang.com' + xiaoqu_url_houduan
            all_url.append(xiaoqu_url)
    pool.map(spider,all_url)
    pool.close()
    pool.join()
