---
title: 14st_day 常用内建模块2
tags: Python
categories：Python学习
toc: true 
---

### hashlib
**MD5**
```
import hashlib
md5 = hashlib.md5()
md5.update('helllo world'.encode('utf-8'))
print(md5.hexdigest())
```
MD5的结果是固定的128 bit字节，通常为32位16进制字符串。
如果数据量大的话，可以使用多个update组合使用，效果和直接使用相同。
**SHA1**
```
import hashlib
sha1 = hashlib.sha1()
sha1.update('hello'.encode('utf-8'))
sha1.update('world'.encode('utf-8'))
print(sha1.hexdigest())
```
SHA1的结果是160 bit字节，通常使用40位的16进制字符串表示。
<!--more-->
### itertools
itertools模块主要提供用于操作迭代对象的函数。
#### chain()
**chain()**可以把一组迭代对象串联起来，形成一个更大的迭代器。
```
>>> for c in itertools.chain('ABC', 'XYZ'):
...     print(c)
# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
```
#### groupby()
**groupby()**把迭代器中相邻的重复元素跳出来放到一起
```
>>> for key, group in itertools.groupby('AAABBBCCAAA'):
...     print(key, list(group))
...
A ['A', 'A', 'A']
B ['B', 'B', 'B']
C ['C', 'C']
A ['A', 'A', 'A']
```

itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。

### contextlib()

任何对象，只要正确实现了上下文管理，都可以使用with语句。
上下文管理通过 ** __enter__和__exit__ ** 这两个方法实现。

#### @contextmanger
```
from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')
```
这样**@contextmange**这个decorator接受一个generator，用yield把with...as var变量输出出去，with语句即可正常工作。
```
with create_query('Bob') as q:
    q.query()
```

