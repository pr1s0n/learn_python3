import requests
location = 'd:/douyin/douyin'
num = 0
def response(flow):
	global num
	path = 'ixigua'
	if path in flow.request.url:
		filename = location + str(num) + '.mp4'
		res = requests.get(flow.request.url)
		with open(filename,'ab') as f:
			f.write(res.content)
			f.flush()
			print('下载完成：{}'.format(filename))
			num += 1