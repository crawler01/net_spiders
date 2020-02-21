import urllib.request as request
# 发起request请求 返回response  http.client.HTTPResponse
response = request.urlopen("https://www.baidu.com/")
# 在http.client.HTTPResponse对象中可以获取到对应的url status 以及读取数据的方法read()
# read()方法返回一个二进制的比特流 0101  但是不方便阅读所以自动给我们转换成了 b'<html>\r\n<head  这种格式
bytes_data = response.read()
# 对字节流进行解码转换成字符串
print(bytes_data.decode("utf-8"))