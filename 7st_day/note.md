### __slots__变量
限制实例的属性
```
class Student(object):
	__slots"__ = ("name","age")

s = Student()
s.name = 'PRI1S0N'
s.age = 20
```
使用__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的