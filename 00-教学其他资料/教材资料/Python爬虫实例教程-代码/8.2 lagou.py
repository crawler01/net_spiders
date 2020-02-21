import requests
from lxml import etree
import time
import csv


def csv_write(item):
    with open('lagou00.csv', 'a', encoding='gbk', newline='') as csvfile:
        writer = csv.writer(csvfile)
        try:
            writer.writerow(item)
        except Exception as e:
            print('write error! ', e)


def spider(list_url):
    r = requests.get(list_url, headers=headers, cookies=cookies)
    time.sleep(2)
    res = r.json()
    for comp in res['content']['data']['page']['result']:
        com_url = 'http://m.lagou.com/jobs/' + str(comp['positionId']) + '.html'
        response = requests.get(com_url, headers=headers, cookies=cookies)
        time.sleep(2)
        sel = etree.HTML(response.text)
        try:
            nianxian = sel.xpath("//span[@class='item workyear']/span/text()")[0].strip()
        except:
            nianxian = ''
        try:
            xueli = sel.xpath("//span[@class='item education']/span/text()")[0].strip()
        except:
            xueli = ''
        try:
            zhize = sel.xpath("string(//div[@class='content'])").strip().replace('\xa0','')
        except:
            zhize = ''
        chengshi = comp['city']
        gongsi = comp['companyName']
        fabushijian = comp['createTime']
        zhiwei = comp['positionName']
        gongzi = comp['salary']
        item = [chengshi, gongsi, fabushijian, zhiwei, gongzi, xueli, nianxian, zhize]
        csv_write(item)
        print('正在抓取：', gongsi)


if __name__ == '__main__':
    headers = {'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Host': 'm.lagou.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
    cookies = {'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1526779144',
 'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1526779124','JSESSIONID': 'ABAAABAAAFDABFG988D00E5BD4C1293C6F3941BF83BDC03','LGRID': '20180520091903-c8b03ea5-5bcb-11e8-8791-5254005c3644','LGSID': '20180520091844-bd06a369-5bcb-11e8-bb0d-525400f775ce','LGUID': '20180520091844-bd06a509-5bcb-11e8-bb0d-525400f775ce','PRE_HOST': 'www.baidu.com','PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc','PRE_SITE': 'https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E5%258B%25BE%26rsv_pq%3D9901c8db0004141f%26rsv_t%3D922dxt%252BpNmZ8Dj7cul7VMEdUmdNr5t%252BZQtNta61WjXEurudfwHkDmLuSlKc%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug3%3D3%26rsv_sug1%3D1%26rsv_sug7%3D100%26rsv_sug2%3D0%26inputT%3D4847%26rsv_sug4%3D5740','PRE_UTM': 'm_cf_cpt_baidu_pc','_ga': 'GA1.3.1292404206.1526779124','_gat': '1','_gid': 'GA1.2.1823262739.1526779124','user_trace_token': '20180520091844-bd06a0b5-5bcb-11e8-bb0d-525400f775ce'}
    all_url = ['http://m.lagou.com/search.json?city=%E5%85%A8%E5%9B%BD&positionName=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&pageNo=' + str(x) + '&pageSize=15' for x in range(1, 180)]
    for url in all_url:
        spider(url)