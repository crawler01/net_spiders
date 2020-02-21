"""
正则表达式应用
1.什么是正则表达式
2.正则表达式的作用
3.常用函数
"""
import re

# match函数从字符串起始位置开始匹配 匹配不成功返回None,匹配成功返回re.Match对象
result = re.match(r'he', 'hello python')
# search函数返回字符串中第一个与正则表达式匹配的re.Match对象 re.I忽略大小写
result = re.search(r'python', 'hello:Python,python is a program language', re.I)
print(result.group())
# split将制定字符串按照正则表达式进行分割
result = re.split(r"-", "hello-python-lol-java")
# findall以列表形式返回全部与正则表达式匹配的字符串
result = re.findall(r"\d+", "hello lucy,age=20,salary=20000")
# sub将与正则表达式匹配的字符串用制定字符串替换掉，返回替换后的字符串
result = re.sub(r"lol", "python", "i like lol, lol is so interesting...")
# compile将正则表达式字符串转换成正则表达式对象Pattern 执行效率更高
pattern = re.compile(r'\d+')
result = re.findall(pattern, '147a258b369c')
print(result)
