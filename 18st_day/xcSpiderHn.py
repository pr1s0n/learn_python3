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