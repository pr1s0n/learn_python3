def gen_func():
	try:
		yield 'http://pr1s0n.com'
	except Exception as e:
		pass

	yield 4
	yield 3
	return 'pr1s0n'

if __name__ == '__main__':
	gen = gen_func()
	print(next(gen))
	gen.throw(Exception,'下载错误')
	print(next(gen))
	gen.throw(Exception,'下载错误')