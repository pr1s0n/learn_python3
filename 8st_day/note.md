
---
title: [8st_day]property/继承/定制类
date: 2019-8-12 17:39
categories: Python学习
tags: python
toc: true
---

<!--more-->

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

### 定制类
#### __iter__
实现__iter__()方法让类可以在for..in循环中使用
该方法返回一个迭代对象，然后python的for循环会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到stopIteration错误时退出循环。
#### __getitem__
把实例当作list，可按照下标取出元素
```
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib()
print(f[0])
```
但是list中可用的切片方法，在这种情况下不可行，原因是__getitem()__ 传入的参数可能是int也可能是一个切片对象，所以要实现切片，需要做判断.
```
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
```
#### __getattr__
动态返回一个属性
当调用不存在的属性时，python会试图从__getattr__(self,*属性值*)中获取属性
```
class Chain(object):
	"""docstring for Chain"""
	def __init__(self, path=''):
		# super(Chain, self).__init__()
		self._path = path
	def __getattr__(self,path):
		return Chain('%s/%s' % (self._path,path))

	def __str__(self):
		return self._path

	__repr__ = __str__

print(Chain().status.user.timeline.list)
```
#### __call__
只要定义一个 __call__()方法，就可以直接对类中的实例进行调用
```
class foo(object):
	def __init__(self,name):
		self.name = name
	def __call__(self)
		print(self.name)
```

