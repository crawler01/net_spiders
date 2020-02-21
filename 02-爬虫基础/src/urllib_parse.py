import  urllib.parse as parser
import  urllib.request as request
paras = {"page":1,"page_num":10}
# 将字典数据转换成参数形式的字符串 page=1&page_num=10
paras_data = parser.urlencode(paras)
# 发起请求
response = request.urlopen("https://www.baidu.com?"+paras_data)
print(response.status)
print(response.url)
