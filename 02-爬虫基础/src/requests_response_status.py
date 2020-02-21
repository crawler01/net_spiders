import requests

# requests请求后，response响应后对应的响应码
# 常见的200 404 500  所有的状态码都存放在requests.codes中
# 通常用response.status_code的响应码和requests.codes码进行对比做逻辑判断
ok = requests.codes.ok
not_found = requests.codes.not_found
internal_server_error = requests.codes.internal_server_error
print("正常响应码：{0}   资源文件不存在：{1}    服务器内部错误：{2}".format(ok, not_found, internal_server_error))
response = requests.get("https://www.baidu.com/")
status_code = response.status_code
if status_code == ok:
    print("向百度请求正常响应..........")
