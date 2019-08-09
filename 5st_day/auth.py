def auth(fn):
	def auth_fn(*args):
		print("————模拟执行权限检查————")
		fn(*args)
		#回调需要装饰的目标函数
	return auth_fn
@auth
def test(a,b):
	print("执行test函数，参数a:%s,参数b:%s" % (a,b))
# 调用test函数，其实是调用装饰后返回的auth_fn函数
test(20,15)
'''
程序执行流程：
1.先执行权限检查
2.回调被修饰的函数。简单来说，auth_fn函数就是为被装饰函数增加了一个权限检查的功能。

结果：
————模拟执行权限检查————
执行test函数，参数a:20,参数b:15
[Finished in 0.2s]
'''