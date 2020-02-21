import requests
# - 通常我们访问服务器资源，通过浏览器代理User-Agent访问
# - 我们可以通过请求时模拟头部headers来模拟为浏览器请求，而不是爬虫
# - 发起请求后也可以再去查看当前请求对应的头部信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
response = requests.get("https://www.baidu.com/", headers=headers)
print(response.status_code)
request_headers = response.request.headers
print(request_headers)
