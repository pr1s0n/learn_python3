---
title: 15st_day HTMLParser
tags: Python
categories: Python学习
toc: true
---

### HTMLParser
#### 非显式调用
```
from urllib import request
from html.parser import HTMLParser
class HtmlParserTest(HTMLParser):
	"""docstring for HtmlParserTest"""
	def __init__(self):
		super().__init__()
		self.tag = None
	def handle_starttag(self,tag,attrs):
		if tag == 'time':
			self.tag = 'Time:'
		elif('class','event-location') in attrs:
			self.tag = 'Location:'
		elif('class','event-title') in attrs:
			self.tag = '\nTitle:'
	def handle_data(self,data):
		if self.tag:
			print(self.tag,data)
	def handle_endtag(self,tag):
		self.tag = None

with request.urlopen('https://www.python.org/events/python-events/') as f:
	html_data = f.read().decode('utf-8')

parser = HtmlParserTest()
parser.feed(html_data)

```
1. **HTMLParser.handle_starttag(tag,attrs)**: 解析时遇到开始标签调用,如`<p class='para'>`,参数tag是标签名,这里是'p',attrs为标签所有属性(name,value)列表,这里是`[('class','para')]`

2. **HTMLParser.handle_endtag(tag)**: 遇到结束标签时调用,tag是标签名

3. **HTMLPars.handle_data(data)**: 遇到标签中间的内容时调用,如`<style> p {color: blue; }</style>`,参数data为开闭标签间的内容.值得注意的是在形如`<div><p>...</p></div>`的位置,并不会在div处调用,而是只在p处调用。

#### 显式调用

1. **HTMLParser.feed(data)**: 参数为需要解析的html字符串,调用后字符串开始被解析

2. **HTMLParser.getpos()**: 返回当前的行号和偏移位置,如(23,5)

3. **HTMLParser.get_starttag_text()**: 返回当前位置最近的开始标签的内容