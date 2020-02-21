"""
BeautifulSoup基本应用
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
# 可以通过soup对象直接访问html的文档节点对象  文档对象.元素名
first_div = soup.div  # 返回文档对象的第一个div对象 注意返回的是带有标签结构的内容
a_tag = soup.ul.li.a  # 返回第一个ul对象的第一个li标签对象下的第一个a标签对象
tag_content = a_tag.string  # 返回标签对象中文本内容  跳转
tag_content2 = a_tag.get_text()  # 返回标签对象中文本内容第二种方式  跳转
tag_attr = a_tag['href']  # 返回标签对象的属性 demo.xml
tag_attr2 = a_tag.get('href')  # 返回标签对象的属性第二种方式 demo.xml
