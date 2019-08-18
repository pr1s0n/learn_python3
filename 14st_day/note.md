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
如果数据量大的话，可以使用多个update组合使用，效果和直接使用相同。
**SHA1**
```
import hashlib
sha1 = hashlib.sha1()
sha1.update('hello'.encode('utf-8'))
sha1.update('world'.encode('utf-8'))
print(sha1.hexdigest())
```
SHA1的结果是160 bit字节，通常使用40位的16进制字符串表示