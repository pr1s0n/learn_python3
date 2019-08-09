def functionA(fn):
	print('A')
	fn()
	return 'fkit'

@functionA
'''
即functionA修饰B，程序将会完成两步操作：
1.将functionB作为functionA的参数，也即是此时functionB = fn,执行functionA时
fn()=>functionB(),输出"B"。
2.将functionB替换成functionA()执行后的结果，即functionA()的返回值'fkit'
整个流程为：先输出functionA()的第一个A,然后是fn()输出B，接着是functionB()打印返回值fkit

'''
def functionB():
	print('B')
print(functionB)