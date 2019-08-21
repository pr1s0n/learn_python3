def gen_func():
	html = yield 'http://pr1s0n.com'
	print(html)
	yield 2
	yield 3
	return 'pr1s0n'

if __name__ == '__main__':
	gen = gen_func()
	url = next(gen)
	html = 'pr1s0n1'
	gen.send(html)
