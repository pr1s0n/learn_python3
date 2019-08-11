class Student(object):
	"""docstring for Student"""
	count = 0
	# name = ''
	def __init__(self, name):
		self.name = name
		Student.count += 1
		print(self.name)
	def get_names(self):
		return self._name
if Student.count != 0:
	print('1')
	print("测试失败")
else:
	bart = Student("bart")
	if Student.count != 1:
		print('2')
		print('测试失败')

	else:
		lisa = Student('lisa')
		if Student.count != 2:
			print('3')
			print('测试失败')
		else:
			print('Students:',Student.count)
			# print('测试通过 %s' % Student.get_names())