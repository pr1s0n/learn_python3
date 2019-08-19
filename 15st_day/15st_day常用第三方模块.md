---
title: 15st_day 常用第三方模块
tags: Python
categories: Python学习
toc: true
---

### Pillow
pillow是一个图形处理模块，可以实现常用的裁剪，模糊，输出文字等功能。

```
from PIL import Image
im = Image.open('image.jpg')
w,h = im.size
print('Original image size:%s %s' % (w,h))
im.thumbnail((w//2, h//2))
print('Resize image to: %s %s' % (w//2,h//2))
im.save('thumbnial.jpg','jpeg')
```
```
from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
```
模糊效果
```
from PIL import Image,ImageFilter
import os
im = Image.open('image.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')
if os.path.exists('blur.jpg'):
	print('success!')
```
### requests
requests用来处理URL资源。
**get()**
使用`requests.get('url')`来实现一个get访问功能。
```
>>> import requests
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
u'{"type":"User"...'
>>> r.json()
{u'disk_usage': 368627, u'private_gists': 484, ...}
```
`requests.status_code`获取状态码
`requests.headers['']`获取头信息
...
如果url带参数，则可以设置get的第二个参数**params**,传入类型为dict.
`requests.content`可以获取网页的bytes对象。
`requests.json`可以直接 获取JSON格式数据，返回值为dict.

**post()**
post请求：
```
>>> r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
```
文件上传：
```
>>> upload_files = {'file': open('report.xls', 'rb')}
>>> r = requests.post(url, files=upload_files)
```
此外，还有**put()**,**delete()**方法，使用方法类似。
如果想要访问时带上cookie，只需要准备一个dict传入cookie参数即可。
```
>>> cs = {'token': '12345', 'status': 'working'}
>>> r = requests.get(url, cookies=cs)
```

### Tkinter图形化界面
```
from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
	"""docstring for Application"""
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	def createWidgets(self):
		# self.helloLabel = Label(self,text='hello world')
		# self.helloLabel.pack()
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self,text='Hello',command=self.hello)
		self.alertButton.pack()
	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message','hello, %s' % name)

app = Application()
app.master.title('hello world')
app.mainloop()	
```
