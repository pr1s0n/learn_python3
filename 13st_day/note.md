### collections
#### namedtuple
**namedtuple**是一个函数，用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，可以用属性来引用tuple的某个元素。
```
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point()
print(p.x)
```
#### deque
`class collections.deque([iterable[, maxlen]])`
返回一个新的双向队列对象，从左到右初始化(用方法 append()) ，从 iterable （迭代对象) 数据创建。如果 iterable 没有指定，新队列为空。
双向队列(deque)对象支持以下方法：

**append(x)**
添加 x 到右端。

**appendleft(x)**
添加 x 到左端。

**clear()**
移除所有元素，使其长度为0.

**copy()**
创建一份浅拷贝。

deque是为了高效实现插入和删除操作的双向列表。

#### ChainMap
**ChainMap**可以把一组dict串起来并组成一个逻辑上的dict。
当程序可以以多种方式传递参数的时候，可以使用ChainMap实现参数的优先级查找，即先查**命令行参数->环境变量->默认参数**
```
from collections import ChainMap
import os,argparse

defaults = {
	
	'color' : 'red',
	'user' : 'gust'
}
parser = argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args()
command_line_args = {k: v for k,v in vars(namespace).items() if v}
combined = ChainMap(command_line_args,os.environ,defaults)
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

```
#### Counter
一个提供一个快捷技术工具。
```

>>> # Tally occurrences of words in a list
>>> cnt = Counter()
>>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
...     cnt[word] += 1
>>> cnt
Counter({'blue': 3, 'red': 2, 'green': 1})

>>> # Find the ten most common words in Hamlet
>>> import re
>>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
>>> Counter(words).most_common(10)
[('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]
```
#### base64
**base64.b64encode(s, altchars=None)**
对 bytes-like object s 进行 Base64 编码，并返回编码后的 bytes。

可选项 altchars 必须是一个长 2 字节的 bytes-like object，它指定了用于替换 + 和 / 的字符。这允许应用程序生成 URL 或文件系统安全的 Base64 字符串。默认值是 None，使用标准 Base64 字母表。

**base64.b64decode(s, altchars=None, validate=False)**
解码 Base64 编码过的 bytes-like object 或 ASCII 字符串 s 并返回解码过的 bytes。

可选项 altchars 必须是一个长 2 字节的 bytes-like object，它指定了用于替换 + 和 / 的字符。

如果 s 被不正确地填写，一个 binascii.Error 错误将被抛出。

如果 validate 值为 False （默认情况），则在填充检查前，将丢弃既不在标准 base-64 字母表之中也不在备用字母表中的字符。如果 validate 为 True，这些非 base64 字符将导致 binascii.Error。
**base64.urlsafe_b64encode(s)**
编码 bytes-like object s，使用 URL 与文件系统安全的字母表，使用 - 以及 _ 代替标准 Base64 字母表中的 + 和 /。返回编码过的 bytes。结果中可能包含 =。
**base64.urlsafe_b64decode(s)**
解码上述加密。
