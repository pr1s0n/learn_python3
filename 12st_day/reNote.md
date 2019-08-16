---
title: st12_day python中的正则表达式
categories: Python学习
tags: Python
toc: true
---
### 正则表达式
[30分钟正则表达式](http://deerchao.net/tutorials/regex/regex.htm)
python中对于正则表达式使用re模块处理
因为python本身也用`\`转义，所以可以在字符串前使用**r**前缀，这样就不用考虑转义问题了。

#### match()
match()方法判断是否匹配成功，然会一个match()对象，否则返回None。
```
import re
test = '字符串'
if re.match(r'正则表达式',test):
	print('ok')
else:
	print('failed')
```
### split()
re模块中的split([正则表达式],[字符串])方法可以使用正则表达式分割字符串，返回值为分割后的字符串字典。

### ()括号分组
使用`()`可以提取分组，`^(\d{3})-(\d{3,8})$`前后为两个组，可以直接从匹配后的字符串中提取出两部分内容。
如果正则表达式中定义了组，那么就可以在match()对象中使用group()方法提取字符串。
group(0)为源字符串，group(1)为第一个子串，group(2)为第二个子串。

### compile()
如果一个正则表达式需要重复使用，那么应该预编译该正则表达式。
**re.compile([正则表达式])**方法用于预编译正则表达式。


