#-*- coding:utf-8 -*-
import requests
from lxml import etree
import csv

def towrite(item):
    with open('doubanriji.csv', 'a',encoding='utf-8') as csvfile:
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
    url = 'https://www.douban.com/accounts/login'
    r1 = requests.get(url,headers = headers)
    html = etree.HTML(r1.text)
    yanzhengma = None
    yanzhengid = None
    try:
        yanzhengurl = html.xpath('//*[@id="captcha_image"]/@src')[0]
        yanzhengid = yanzhengurl.split('=')[1].split('&')[0]
        t1 = requests.get(yanzhengurl)
        with open('yanzhengma.jpg','wb') as f:
            f.write(t1.content)
        from PIL import Image
        img = Image.open('yanzhengma.jpg')
        img.show()
        yanzhengma = input(u'请输如验证码：')
    except:
        pass
    formdata = {'source':'index_nav','form_email':'984595060@qq.com','form_password':'beijing1234','captcha-solution':yanzhengma,'captcha-id':yanzhengid}
    s = requests.session()
    r = s.post(url,data = formdata)
    selector = etree.HTML(r.text)
    wenzhangs = selector.xpath('//div[@data-uid = "900117594"]')
    for i in range(len(wenzhangs)):
        yonghu = selector.xpath('//*[@class = "lnk-people"]/text()')[i]
        title = selector.xpath("//div[@class = 'title']/a/text()")[i]
        item = [yonghu,title]
        towrite(item)
        print(u'正在保存: %s 的日记' % yonghu)

