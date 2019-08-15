### IO编程
#### 读文件
**open('路径','模式',encoding='编码方式',errors='ignore')**
1. 打开文本文件使用'r',二进制文件使用'rb'
2. 编码方式默认为UTF-8
3. 遇到编码错误后使用error参数处理

每次打开文件操作结束后需要使用f.close()关闭文件，不然会持续造成内存占用。
可以使用with语句简化操作。
#### 写文件
**write([str])**
write()方法用于向文件中写入指定字符串，参数为字符串，返回值为写入的字符长度。
和open()参数配合with使用
```
with open('/test/test.txt','w') as f:
	f.write('hello')
```
需要注意的是，以**w**模式写入文件时，默认是覆盖原有文件的所有内容，如果需要将字符串追加到文件末尾，则可以使用'a'模式写入。

#### os模块
首先使用`import os`将os模块加载进来
1. os.name *返回操作操作系统类型，posix为Linux、Unix或Mac os x，nt为Windows操作系统。*
2. os.uname *返回详细的系统信息，但是Windows不可使用*
3. os.environ *返回系统中定义的环境变量，如果需要获取某个变量的值，可以调用os.environ.get()*


#### 操作文件和目录
```
# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('D:\\', 'test')
'D:\\test'
# 然后创建一个目录:
>>> os.mkdir('/test')
# 删掉一个目录:
>>> os.rmdir('/test')
```
**注意，因为在Linux和Windows中目录分割符号不同，所以在拼接和拆分目录结构时不要直接拼接字符串，而要使用`os.path.join()`和`os.path.split()`函数操作**

`os.path.splitext()`函数可以直接获取到文件扩展名
**shutil**模块中提供了很多os模块没有的实用功能，可以看作是os的扩展补充。

列出当前目录下的所有目录：
```
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['$RECYCLE.BIN', 'blog', 'douyin', 'download', 'Huorong', 'learn_python3', 'nodejs', 'sublime', 'System Volume Information', 'Test404 HTTP Fuzzer', 'vedio']
```
列出所有的.py后缀的文件
```
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['class.py', 'classes.py', 'sys_hello.py']
>>>
```
