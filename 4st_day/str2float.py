from functools import reduce
def str2float(s):
	s_1 = s[:s.index('.')]
	s_2 = s[s.index('.')+1:]
	def fn(x, y):

		return x * 10 + y
	def char2num(h):
		digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
		return digits[h]
	s1 = reduce(fn, map(char2num,s_1))
	s2 = reduce(fn, map(char2num,s_2))
	return s1 + s2 / 10 ** len(s_2)
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
	print('测试成功!')
else:
	print('测试失败!')