### 调试
#### assert
```
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
```
assert表示：如果n != 0 得结果为true,则程序继续进行
如果断言失败，assert语句本身就会抛出AssertionError错误，内容为表达式后的'n is zero!'
python解释器可以使用-O参数来关闭assert

#### logging
import logging
logging.basicConfig(level=logging.INFO)

logging不会抛出错误，且可以输出错误信息到文件。
logging记录的信息等级有：debug,info,warning,error等几个级别。

#### pdb
pdb适用于python解释器，可使程序一步一步运行。
```
(Pdb) n
> /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
-> n = int(s)
(Pdb) n
> /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
-> print(10 / n)
```

使用**n**可以单步执行代码，使用**p 变量名**查看变量
```
(Pdb) p s
'0'
(Pdb) p n
0
```
使用**q**结束调试

#### pdb.set_trace()
程序内使用pdb.set_trace()可以设置一个断点。
运行后，程序会在断点处暂停并进入pdb调试环境
