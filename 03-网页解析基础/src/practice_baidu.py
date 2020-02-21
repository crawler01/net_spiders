"""
获取百度头部的链接信息和文字
①查看网页分析结构 找到包含链接的div
②requests发起请求
③返回内容用lxml的etree构建element对象
④利用xpath抽取内容
"""
import requests
from lxml import etree

url = "https://www.baidu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
# ②requests发起请求
response = requests.get(url, headers=headers)
# ③返回内容用lxml的etree构建element对象
element = etree.HTML(response.content.decode("utf-8"))
# ④利用xpath抽取内容
div_element_content = element.xpath('//*[@id="u1"]/a/text()')
print(div_element_content)
div_element_attr = element.xpath('//*[@id="u1"]/a/@href')
print(div_element_attr)