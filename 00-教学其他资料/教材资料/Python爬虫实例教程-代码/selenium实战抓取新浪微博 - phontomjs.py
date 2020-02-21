from selenium import webdriver
import csv
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def towrite(item):
    with open('weibo.csv', 'a',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        try:
            print('正在写入')
            writer.writerow(item)
        except:
            print('write error!')

def spider():
    driver.get("https://m.weibo.cn/")
    time.sleep(4)
    all_weibo = driver.find_elements_by_xpath\
    ('//*[@class="card card9 line-around"]')
    for weibo in all_weibo:
        fabuid = weibo.find_elements_by_xpath\
        ('header/div/a/span')[0].text
        fabu_neirong = weibo.find_elements_by_xpath\
        ('section')[0].text
        item = [fabuid, fabu_neirong]
        print('成功抓取')
        towrite(item)

def denglu():
    driver.get(login_url)
    time.sleep(3)
    driver.set_window_size(1920, 1080)
    username = driver.find_element_by_xpath \
        ('//*[@id="loginName"]')
    username.send_keys('13439316993')
    password = driver.find_element_by_xpath \
        ('//*[@id="loginPassword"]')
    password.send_keys('beijing1234')
    submit = driver.find_element_by_xpath \
        ('//*[@id="loginAction"]')
    print('准备登录')
    submit.click()


if  __name__ == '__main__':
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    )
    login_url = 'https://passport.weibo.cn/signin/login?' \
            'entry=mweibo&res=wel&wm=3349&' \
            'r=http%3A%2F%2Fm.weibo.cn%2F'
    driver = webdriver.PhantomJS\
    (executable_path = 'd:/selenium/phantomjs.exe',
     desired_capabilities = dcap)
    denglu()
    time.sleep(3)
    spider()