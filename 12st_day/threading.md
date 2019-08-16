### 多线程
任何进程默认都会启动一个线程，这个线程被称为主线程，主线程又可以启动新的线程。
threading模块中的**current_thread()**函数，永远返回当前线程的实例。主线程实例的名字为`MainThread`,子线程的名字在创建时指定。名字没啥意义，就是需要的时候可以打印出来。

#### Lock
多进程中，同一个变量，各自有一份拷贝存在于每个进程中；多线程中，所有变量都由所有线程共享。
所以为了避免多个线程使变量错乱，需要给线程加锁，防止线程之间修改出现冲突。当一个线程获得锁之后，其他线程就不能同时执行该线程运行中的方法，只能等待锁被释放后才可以更改。无论多少线程，同一时刻只有一个线程持有该锁，所以不会造成修改的冲突。
**threading**模块中的**lock()**方法可以创建一个锁。
```
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
```
锁在用完后一定要释放，否则其他线程将会变成死线程。

多线程编程时，模型复杂，容易发生冲突，必须加锁隔离线程，同时也要小心死锁。

python解释器设计时有GIL全局锁，所以python多线程无法利用多核。

### ThreadLocal
```
import threading
local_school = threading.local()
def process_student():
	std = local_school.student
	print('hello %s (in %s)' % (std,threading.current_thread().name))
def process_thread(name):
	local_school.student = name
	process_student()

t1 = threading.Thread(target=process_thread,args=('Lihua',),name='线程A')
t2 = threading.Thread(target=process_thread,args=('Hanmeimei',),name='线程B')
t1.start()
t2.start()
t1.join()
t2.join()

```
一个ThreadLocal变量虽然是全局变量，但是每个线程都只能操作自己线程内的变量副本，互不干扰。就像班里的点名簿，每个班都有可能有一个叫李华的同学，但是每个班在点名时点的是本班的李华，和其他班的重名同学不是一个人。

