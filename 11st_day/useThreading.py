import time
import threading
def loop():
	print('线程 %s 正在运行' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('线程 %s >>> %s' % (threading.current_thread().name,n))
		time.sleep(1)

	print('线程 %s 结束' % threading.current_thread().name)

print('线程 %s 正在运行' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('线程 %s 结束' % threading.current_thread().name)
