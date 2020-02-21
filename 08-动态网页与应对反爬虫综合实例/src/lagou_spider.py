"""
需求：采集拉勾网移动端对应检索职位的数据采集，将采集的数据保存到csv文件中
分析：
    1.分析拉勾网移动端动态数据的获取链接url地址
    2.根据对应的数据请求地址发起请求返回对应的json数据
    3.当拿到对应的职位列表数据后从中抽取对应的positionId构建详情页url地址
    4.请求详情页url地址内容，解析对应的目标数据进行csv写入数据
    5.解决反爬虫问题
实现：
    1.编写写入csv数据函数
    2.根据传入的关键字和页码数字构建对应的列表页url地址
    3.对列表页url地址发起请求处理返回数据发起详情页请求并抽取数据，写入数据

注意反爬虫问题：
    1.直接请求数据连接时不能正常返回数据，因为反爬虫
      解决方案：每次请求带上第一次方法初始页面的cookie并设置Referer值
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
    with open("jobs.csv", "a", encoding='gbk', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(items)


def send_request(url):
    """
      给目标url地址requests请求,注意这里添加了处理发爬虫代码
      :param url: 目标url资源地址
      :return: 返回响应对象
      """
    headers = {
        'Referer': 'https://m.lagou.com/search.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    session = requests.session()
    session.get('https://m.lagou.com/search.html', headers=headers, timeout=3)
    cookies = session.cookies
    response = requests.get(url, headers=headers, cookies=cookies, timeout=5)
    return response


def get_pages_url(key, pages):
    """
    根据检索的关键字和希望获取的页码值获取对应的url链接
    :param key:搜索关键字
    :param pages:一共希望获取多少页数据
    :return:返回url链接地址列表
    """
    search_url = []
    for page in range(1, pages + 1):
        search_url.append('https://m.lagou.com/search.json?city=%E5%85%A8%E5%9B%BD&positionName=' + key + '&pageNo=' + str(page) + '&pageSize=15')
    return search_url


def get_job_data(page_url):
    """
    根据传入的分页列表数据发起请求，返回数据得到列表中的每个职位的positionId
    根据positionId拼接处对应的职位url地址，发起请求获取对应的信息
    获取 年限要求 学历要求 职位描述 城市信息 公司名称 发布时间 职位名称 工资信息等
    :param page_url:分页url地址
    :return:抽取数据写入文件
    """
    page_data = send_request(page_url).json()
    for job in page_data['content']['data']['page']['result']:
        job_url = 'https://m.lagou.com/jobs/' + str(job['positionId']) + '.html'
        job_elements = etree.HTML(send_request(job_url).text)
        items = [job_elements.xpath('//*[@id="content"]/div[2]/div[1]/span[4]/span/text()')[0].strip(),  # 年限要求
                 job_elements.xpath('//*[@id="content"]/div[2]/div[1]/span[5]/span/text()')[0].strip(),  # 学历要求
                 job_elements.xpath('string(//*[@id="content"]/div[4]/div)').strip().replace('\xa0', '').replace('\ufeff', ''),  # 职位描述
                 job['city'],  # 城市信息
                 job['companyFullName'],  # 公司名称
                 job['createTime'],  # 发布时间
                 job['positionName'],  # 职位名称
                 job['salary']  # 工资信息等
                 ]
        write_data(items)

if __name__ == '__main__':
    page_urls = get_pages_url("数据分析", 3)
    for page_url in page_urls:
        get_job_data(page_url)
