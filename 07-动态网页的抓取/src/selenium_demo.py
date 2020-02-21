"""
需求：用Selenium模拟一次手动打开百度首页，键入python关键字进行搜索
"""
from selenium import webdriver
# 导入Selenium，启动驱动器
driver = webdriver.Chrome("D:/tools/selenium/chromedriver.exe")
# 使用webdriver打开百度首页
driver.get("https://www.baidu.com/")
# 使用xpath找到搜索框
input = driver.find_element_by_xpath('//*[@id="kw"]')
# 找到搜索框键入关键字
input.send_keys('python')
# 模拟点击按钮
driver.find_element_by_xpath('//*[@id="su"]').submit()