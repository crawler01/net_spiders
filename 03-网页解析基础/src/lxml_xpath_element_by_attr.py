"""利用xpath语法 根据元素的属性查找对应的元素对象"""
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
# 使用元素对象的属性查找对应的元素 主要在xpath语法中用@属性名=属性值 定位
element_div = element.xpath('//div/div[@class="header"]/text()')
print(element_div)