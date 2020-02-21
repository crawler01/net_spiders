# - requests发起的所有请求返回值对象都是response
# - response返回的内容可以通过text和content属性进行获取
# - response.text和response.content的区别在于前者返回文本，后者以字节方式返回
# - 如果请求一张图片回来直接保存则用response.content
# - 可以获取返回内容的字符集或者重新设定字符集
import requests
response = requests.get("https://www.baidu.com/")
response_text = response.text
response_content = response.content
response_encoding = response.encoding
print(response_text)
print(response_content)
print(response_encoding)
