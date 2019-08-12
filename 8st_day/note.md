### @property装饰器
把一个方法变成属性调用
好处是方便调用
```
class Student(object):
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		#此处省略检查是否参数合法
		self._score = value
```
只使用@property而不不对该函数setter方法，表示定义为只读属性
```
class Screen(object):
	"""docstring for Screen"""
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		self._width = value

	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,value):
		self._heigth = value
	@property
	def resolution(self):
		return self._heigth * self._width
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
```

### 多重继承
使用方法
```
class Animal(object):
	def __init__(self):
		print('this is an Animal!')

class Runable(object):
	def run(self):
		print('Running...')

class Flyable(Animal):
	def fly(self):
			print('Flying...')

class Dog(Animal,Runable):
		def dog(self):
			return print('dog')
dogs = Dog()
dogs.run()
dogs.dog()
```

### MixIn多重继承

因为python允许使用多重继承，所以MixIn为常见写法