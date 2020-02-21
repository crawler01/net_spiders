"""
使用requests会话对象模拟登陆
1.添加请求头部
2.初始化一个requests会话对象
3.准备post参数发起post请求
4.响应数据检测是否登陆成功
"""
import requests


def login(url, data):
    """
    :param url:
    :param data:
    :return:
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    session = requests.session()
    response = session.post(url, data, headers=headers)
    print(response.text)
    # print(session.get("https://accounts.douban.com",headers=headers).text)


if __name__ == '__main__':
    url = "https://accounts.douban.com/j/mobile/login/basic"
    data = {"name": "18166480690", 'password': 'root123', 'remember': 'false'}
    login(url, data)
