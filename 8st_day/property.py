class Student(object):
	"""docstring for Student"""
	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self,values):
		self._birth = values

	@property
	def age(self):
		return 2019 - self._birth
	
s = Student()
s.birth = 1999
print(s.age)
