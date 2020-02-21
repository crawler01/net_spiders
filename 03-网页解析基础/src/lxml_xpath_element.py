"""根据xpath查找对应的元素对象"""
from lxml import  etree
html = """
	<body>
		<div id="main">
			<div class="header">header内容</div>
			<div>不要叫我<span class="madam">宅女</span>，请叫我<span class="madam">居里夫人</span></div>
			<div>最近总是失眠，16小时就醒一次</div>
			<div>人人都说我<span class="look">丑</span>，其实我只是<span class="look">美</span>得不明显</div>
			<div>上帝欲使其灭亡,必先使其疯狂</div>
			<div>说假话总会<span class="result">被人揭穿</span>,戴假发总会<span class="result">被风揭穿</span></div>
			<div>脑袋空不要紧,关键是不要进水</div>
		</div>
	</body>
"""
element = etree.HTML(html)
# 返回lxml.etree._Element对象，调用该对象的xpath方法
# xpath语法从/开始后面跟上对应的的标签，可以追加属性，可以获取文本内容
element_div = element.xpath('//body/div/div[1]/text()')
print(element_div)