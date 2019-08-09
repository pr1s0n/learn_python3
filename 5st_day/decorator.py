# -*- coding: utf-8 -*-
import time,functools
def metric(fn):
	def wrapper(*args,**kw):
		start=time.time()
		fn(*args,**kw)
		end=time.time()
		print('%s executed in %s ms' % (fn.__name__, (end-start)))
		return fn(*args,**kw)
	return wrapper
@metric
def fast(x, y):
	time.sleep(0.0012)
	return x + y;

@metric
'''
slow被metric装饰，meric返回一个wrapper函数，则调用slow函数即是调用wrapper函数

'''
def slow(x, y, z):
	time.sleep(0.1234)
	return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
	print('测试失败!')
elif s != 7986:
	print('测试失败!')

