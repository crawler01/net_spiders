"""
需求：使用Selenium库采集新浪微博数据
分析：
    1.编写落地csv文件函数
    2.编写登陆新浪微博函数
    3.编写爬取 解析自己发布的微博内容
"""
import csv
import time

from selenium import webdriver


def write_data(items):
    """
    实现将列表数据写入csv文件
    :param items:列表数据
    :return:将内容写入文件无返回值
    """
    with open("weibo.csv", "a", encoding='gbk', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(items)


def login():
    """
    使用Selenium模拟登陆微博
    :return:
    """
    driver.get("https://weibo.com/")
    time.sleep(5)
    driver.set_window_size(1920, 1080)
    # 输入用户名
    uname = driver.find_element_by_xpath('//*[@id="loginname"]')
    uname.send_keys('18166480690')
    # 输入密码
    # time.sleep(5)
    password = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
    password.send_keys('python00')
    # 点击登陆按钮
    # time.sleep(5)
    submit = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
    print('登陆中.....')
    submit.click()
    time.sleep(5)


def spider():
    """
    登陆微博后采集自己发布的微博内容
    :return:
    """
    driver.get("https://weibo.com/")
    time.sleep(5)
    all_weibo = driver.find_elements_by_xpath('//*[@class="WB_cardwrap WB_feed_type S_bg2 WB_feed_like"]')
    for weibo in all_weibo:
        pub_id = weibo.find_elements_by_xpath('div[1]/div[3]/div[1]/a[1]')[0].text
        pub_url = weibo.find_elements_by_xpath('div[1]/div[3]/div[2]/a[1]')[0].get_attribute('href')
        pub_content = weibo.find_elements_by_xpath('div[1]/div[3]/div[4]')[0].text
        write_data([pub_id,pub_url,pub_content])

if __name__ == '__main__':
    driver = webdriver.Chrome("D:/tools/selenium/chromedriver.exe")
    login()
    spider()
