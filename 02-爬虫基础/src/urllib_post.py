from urllib import request, parse
# 需要传递的post参数
post_data = parse.urlencode([("key1", "value1"), ("key2", "value2")])
print(post_data)  # key1=value1&key2=value2
# 模拟一个浏览器请求
req = request.Request("https://www.baidu.com")
# 添加请求头部
req.add_header("User-Agent",
               "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
# 发起post请求  注意这里data传递的参数必须是bytes类型
response_data = request.urlopen(req,data=post_data.encode('utf-8')).read().decode()
print(response_data)
