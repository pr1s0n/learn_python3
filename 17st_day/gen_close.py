def gen_func():

	yield 'http://pr1s0n.com\n'
	yield 2
	yield 3
	return 'pr1s0n'

if __name__ == '__main__':
	gen = gen_func()
	print(next(gen))
	gen.close()
	next(gen)

#GeneratorExit继承自baseException