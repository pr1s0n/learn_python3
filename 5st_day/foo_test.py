def func(fn):
	def bar(*args):
		print("==1==",args)
		n = args[0]
		print("==2==",n * (n - 1))
		print(fn.__name__)
		fn(n * (n - 1))
		print("*" * 15)
		return fn(n * (n - 1))
	return bar
@func
'''
装饰器效果相当于：func(test)
test将会替换成该语句的返回值
由于func函数返回bar函数，因此funcB就是bar
'''
def test(a):
	print("==test-functions==",a)
print(test)
test(10)
test(6,5)
'''
上面程序定义了一个装饰器函数func，该函数执行完成后返回bar函数，这意味着被@func
修饰的函数最终都会被替换成bar函数

使用@func修饰test函数，程序执行func(test)，并将test替换成func函数的返回值：
bar函数，此时test已经被替换成bar函数，接下来程序两次调用test函数，其实就是
调用bar函数。

'''