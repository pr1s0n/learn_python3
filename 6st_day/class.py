class Student(object):
	"""docstring for Student"""
	def __init__(self, name,gender):
		super(Student, self).__init__()
		self.__name = name
		self.__gender = gender

	def get_gender(self):
		return self.__gender
	def set_gender(self,gender):
		if gender in ["sale","female"]:
			self.__gender = gender

bart = Student('bart','male')
if bart.get_gender() != 'male':
	print("测试失败")
else:
	bart.set_gender('female')
	if bart.get_gender() != 'female':
		print("测试失败")
	else:
		print("测试成功")