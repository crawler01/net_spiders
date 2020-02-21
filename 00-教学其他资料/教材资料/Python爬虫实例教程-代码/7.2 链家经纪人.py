import requests
import csv
import time
from lxml import etree


def csv_writer(item):
    with open('lianji_jingjiren.csv', 'a', encoding='gbk', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(item)


def spider(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
    response = requests.get(url, headers=headers)
    time.sleep(5)
    sel = etree.HTML(response.text)
    agent_list = sel.xpath('//li[@class="pictext flexbox box_center_v"]')
    for agent in agent_list:
        agent_name = agent.xpath('div[2]/div[1]/span[1]/a/text()')[0]
        agent_region = agent.xpath('div[2]/div[2]/span[1]/text()')[0]
        item = [agent_name, agent_region]
        print('正在爬取：', agent_name)
        csv_writer(item)

if __name__ == '__main__':
    for i in range(1, 3):
        url = 'https://m.lianjia.com/bj/jingjiren/?page_size=15&_t=1&offset=' + str(i*15)
        spider(url)