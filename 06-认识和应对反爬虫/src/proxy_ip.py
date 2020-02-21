"""
临时代理ip：https://www.xicidaili.com/nn
设置代理IP：
    在调用requests的get函数时传入proxies参数
    proxies参数结构是一个数据字典型数据
    可以设置多个代理ip
"""
import requests


def is_vaild_ip(proxies):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }
    try:
        response = requests.get("http://www.baidu.com", headers=headers, proxies=proxies, timeout=5)
    except:
        return False
    else:
        return True


if __name__ == '__main__':
    proxies = {'http': 'http://180.122.147.97:20694'}
    print(is_vaild_ip(proxies=proxies))
