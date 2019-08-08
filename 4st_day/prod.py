#-*- coding:utf-8 -*-
from functools import reduce
def prod(L):
	def function(x,y):
		return x*y
	return reduce(function,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('成功!')
else:
    print('失败!')