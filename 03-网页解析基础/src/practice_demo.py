from lxml import  etree
html = """
	<body>
		<div id="main">
			id为main的内容
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
# 获取所有div元素
div_ele = element.xpath("//div")
# 获取id为main的div元素
div_main = element.xpath('//div[@id="main"]')
# 获取id为main的第二个子div元素的内容
div_txt = element.xpath('//div[@id="main"]/div[2]/text()')
# div_txt = element.xpath('string(//div[@id="main"]/div[2])')
# 获取所有span元素的class属性值
span_class = element.xpath('//span/@class')
# 获取所有div元素内容
div_content = element.xpath('string(//div)')
print(div_content)
# 获取所有span元素内容
span_content = element.xpath('//span/text()')
print(span_content)
