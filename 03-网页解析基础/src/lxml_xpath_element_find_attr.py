"""利用xpath语法 提取元素对应的属性"""
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
			12
		</div>
	</body>
"""
element = etree.HTML(html)
# xpath可以快速定位到元素 同时可以快速定位元素的属性值 @属性名
# 需求：获取所有span标签的class属性
span_class = element.xpath('//div/span/@class')
print(span_class)
