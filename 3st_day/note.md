###迭代

如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历成为迭代。

在python中，迭代是通过for...in来完成的。

使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行。

###生成器

在python中，一边循环一边计算的机制，称为生成器：generator

如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

generator和函数的执行流程不一样，函数时顺序执行，遇到return语句或者最后一行函数语句就会返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

###迭代器
凡是可以作用于for循环的对象都是Iterable类型
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
集合数据类型时Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
