"""
BeautifulSoup选择器find_all方法应用
"""
from bs4 import BeautifulSoup

html = """
 	<body>
		<div id="main">
			id为main的内容
			<div class="header">header内容</div>
			<div>不要叫我宅女，请叫我居里夫人</div>
			<div>最近总是失眠，16小时就醒一次</div>
			<div>人人都说我丑，其实我只是美得不明显</div>
			<div>上帝欲使其灭亡,必先使其疯狂</div>
			<div>说假话总会被人揭穿,戴假发总会被风揭穿</div>
			<div>脑袋空不要紧,关键是不要进水</div>
			<ul>
			    <li><a href="demo.xml">跳转</a></li>
			    <li><a href="demo3.xml">跳转3</a></li>
			</ul>
		</div>
	</body>
"""
# bs4解析器调用BeautifulSoup的构造方法将字符串转换成BeautifulSoup文档对象
soup = BeautifulSoup(html, 'lxml')
# 根据标签名查找所有对应的元素
all_div = soup.find_all('div')
# 根据下标查找指定某个元素
div_1 = soup.find_all('div')[1]
# 获取元素文本内容
print(div_1.string)
print(div_1.get_text())
# 根据属性查找元素节点
div_by_attr = soup.find_all(attrs={'class': 'header'})[0]
div_by_class = soup.find_all(class_='header')  # 注意class有一个下划线
div_by_id = soup.find_all(id='main')

