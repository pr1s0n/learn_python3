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