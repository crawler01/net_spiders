from selenium import webdriver
import csv
import time

def login():
    driver.get('https://weibo.com')
    time.sleep(5)
    driver.set_window_size(1920, 1080)
    username = driver.find_element_by_xpath('//*[@id="loginname"]')
    username.send_keys('baipon@163.com')
    password = driver.find_element_by_name('password')
    password.send_keys('15615431215')
    submit = driver.find_element_by_xpath('//*[@class="W_btn_a btn_32px"]')
    print('准备登录....')
    submit.click()
    time.sleep(3)

def spider():
    driver.get('https://weibo.com')
    time.sleep(4)
    all_weibo = driver.find_elements_by_xpath('//div[@class="WB_cardwrap WB_feed_type S_bg2 WB_feed_like"]/div')
    for weibo in all_weibo:
        pub_id = weibo.find_elements_by_xpath('div[3]/div[1]/a[1]')[0].text
        pub_id_url = weibo.find_elements_by_xpath('div[3]/div[1]/a[1]')[0].get_attribute('href')
        pub_content = weibo.find_elements_by_xpath('div[3]/div[3]')[0].text
        item = [pub_id,pub_id_url, pub_content]
        print('成功抓取')
        csv_writer(item)

def csv_writer(item):
    with open('weibo.csv', 'a', encoding='gbk', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(item)

if  __name__ == '__main__':
    driver = webdriver.Chrome(r'E:\pachong2\chromedriver.exe')
    login()
    while True:
        spider()
        time.sleep(60)