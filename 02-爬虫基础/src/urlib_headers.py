import urllib.request as request

# 模拟浏览器头部
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
# 创建一个带有头部的request请求
req = request.Request("https://www.baidu.com", headers=headers)
# 发起请求 返回响应
response = request.urlopen(req)
print(response.read().decode())
