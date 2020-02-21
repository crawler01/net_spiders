"""
    在代码中模拟cookie请求，检测是否能访问豆瓣中已经登陆的数据
    1.在豆瓣网先登陆
    2.将豆瓣网中的cookie信息保存到请求headers中
    3.requests模拟发起请求
    4.检测是否能访问到登陆后的信息
"""
import requests

_base_url = "https://www.douban.com/"


def send_requests(url, cookie_str):
    """
    使用请求url地址和cookie字符串发起request请求
    :param url:目标url资源
    :param cookie_str:cookie字符串
    :return:返回响应后的字符串
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    response = requests.get(_base_url, headers=headers, cookies=parse_cookie(cookie_str))
    return response.text


def parse_cookie(cookie_str):
    """
    将字符串形式的cookie内容转换为字典格式
    :param cookie_str:字符串形式的cookie
    :return:返回cookie字典
    """
    cookies = {}
    for key_value in cookie_str.split(';'):
        key, value = key_value.split('=', 1)
        cookies[key.strip()] = value.replace('"', '')
    return cookies


def checkLogin(url, cookie_str):
    """
    检测返回的数据中是否包含已经登陆的用户数据
    :param url:请求目标地址
    :param cookie_str:字符串形式的cookie
    :return:存在返回True否则返回False
    """
    response_text = send_requests(url, cookie_str)
    if "crawler" in response_text:
        return True
    else:
        return False


if __name__ == '__main__':
    cookie_str = 'll="108309"; bid=hUQr60pjsUQ; _pk_ses.100001.8cb4=*; __utma=30149280.984375261.1577407615.1577407615.1577407615.1; __utmz=30149280.1577407615.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); push_noty_num=0; push_doumail_num=0; __utmv=30149280.20191; __yadk_uid=DdYYzYz9DVjsjBo5lhra1Win5zkTxmy6; ap_v=0,6.0; __utmc=30149280; __utmt=1; dbcl2="201913528:ns6STqvB3/I"; ck=aT2U; _pk_id.100001.8cb4=c4d02c85853adae9.1577407613.1.1577410561.1577407613.; __utmb=30149280.20.10.1577407615'
    print(checkLogin(_base_url, cookie_str))
