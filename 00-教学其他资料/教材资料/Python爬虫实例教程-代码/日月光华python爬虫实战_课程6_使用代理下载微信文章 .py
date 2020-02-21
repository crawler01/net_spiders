import requests
from lxml import etree

def spider(url):
    r = requests.get(url,headers = headers)
    return etree.HTML(r.text)

def get_all_url(yeshu,neirong):
    for sousuoye in range(1,int(yeshu)+1):
        sousuo_url = 'http://weixin.sogou.com/weixin?query=' + neirong + "&_sug_type_=&s_from=input&_sug_=y&type=2&page=" + str(sousuoye) + '&ie=utf8'
        selector = spider(sousuo_url)
        meiye_url = selector.xpath("//*[starts-with(@id,'sogou_vr_11002601_title_')]/@href")
        all_url.extend(meiye_url)
        
def spider_xiangqing(url):
    selector = spider(url)
    title = selector.xpath('//h2[@class = "rich_media_title"]/text()')[0].strip()
    neirong = selector.xpath('string(//*[@id = "img-content"])')
    wenzi = neirong.strip()
    wenzi.encode('utf-8')
    towrite(wenzi,title)
        
def towrite(item,title):
    try:
        with open('./wenjian/' + title.replace('|','') + '.txt','wt',encoding='utf-8') as f:
            f.write(item)
            print('正在下载：',title)
    except:
        print('下载失败：',title)
    
    
if  __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
    proxies = {
#      "http": "http://219.138.58.71:3128",
#      "http": "http://122.114.31.177:808",
      "http": "http://61.135.217.7:80",
      "https": "https://60.184.182.204:8118",
    }
    sousuoneirong = input('请输入搜索内容：')
    sousuoyeshu = input('请输入搜索页数（必须为自然数）：')
    all_url = []
    get_all_url(sousuoyeshu,sousuoneirong)
    for url in all_url:
        spider_xiangqing(url)