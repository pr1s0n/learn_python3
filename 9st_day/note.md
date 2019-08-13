### type()函数
type()函数既可以返回一个对象的类型，又可以创建出新的类型。
type('类名',(继承的父类),dict(方法绑定函数))
使用type()函数创建的类和直接写class完全一样，因为python解释器遇到class定义时，仅仅是扫描以下class定义的语法，然后调用type()函数创建出class。

### metaclass()
当我们定义了类之后，可以根据这个类创建出实例，所以：
先定义metaclass，就可以创建类，最后创建实例。

### 错误处理
#### try
try...excepy...finally
流程为：try产生错误跳转到except，except执行结束后如果又finally则跳转到finally。
