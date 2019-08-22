### 普通爬虫和协程爬虫
#### 普通爬虫逻辑：
```
import time
from lxml import etree
import requests
urls = [
	'https://henan.qq.com/a/20190822/001115.htm',
	'https://henan.qq.com/a/20190822/001128.htm',
	'https://henan.qq.com/a/20190822/001086.htm',
	'https://henan.qq.com/a/20190822/001764.htm',
	'https://henan.qq.com/a/20190822/001163.htm',
	'https://henan.qq.com/a/20190822/001169.htm',
	'https://henan.qq.com/a/20190822/001196.htm',
	'https://henan.qq.com/a/20190822/001278.htm'
]
url = 'https://henan.qq.com/a/20190822/001764.htm'
def get_titles(url,cnt):
	reponse = requests.get(url)
	html = reponse.content
	title = etree.HTML(html).xpath('//*[@id="Main-Article-QQ"]/div[2]/div[1]/div[2]/div[1]/h1/text()')
	print('第%d个title:%s' % (cnt,''.join(title)))

if __name__ == '__main__':
	start1 = time.time()
	i = 0
	for url in urls:
		i = i + 1
		start = time.time()
		get_titles(url,i)
		print('第%d个title爬取耗时:%.5f秒' % (i,float(time.time() - start)))
	print('爬取总耗时:%.5f秒' % float(time.time() - start1))
```
**get_titles()**函数首先使用**requests**模块发起了一个get请求，获取html的页面源码。
然后利用**etree**中的**xpath**解析出想要获取到的内容。
xpath('')中使用的是xpath语法，可以准确的定位获取到的内容。可以在审查元素中直接右键**Copy->Copy Xpath**复制出xpath代码，然后使用时在尾部加上**text()**就可以。

#### 协程爬虫
```
import time
from lxml import etree
import aiohttp
import asyncio
urls = [
	'https://henan.qq.com/a/20190822/001115.htm',
	'https://henan.qq.com/a/20190822/001128.htm',
	'https://henan.qq.com/a/20190822/001086.htm',
	'https://henan.qq.com/a/20190822/001764.htm',
	'https://henan.qq.com/a/20190822/001163.htm',
	'https://henan.qq.com/a/20190822/001169.htm',
	'https://henan.qq.com/a/20190822/001196.htm',
	'https://henan.qq.com/a/20190822/001278.htm',
]
titles = []
sem = asyncio.Semaphore(10)
async def get_title(url):
	with(await sem):
		async with aiohttp.ClientSession() as session:
			async with session.request('GET',url) as resp:
				html = await resp.read()
				title = etree.HTML(html).xpath('//*[@id="Main-Article-QQ"]/div[2]/div[1]/div[2]/div[1]/h1/text()')
				print(''.join(title))

def main():
	loop = asyncio.get_event_loop()
	tasks = [get_title(url) for url in urls]
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()
if __name__ == '__main__':
	start = time.time()
	main()
	print('总耗时: %.5f秒' % float(time.time()-start))
```
