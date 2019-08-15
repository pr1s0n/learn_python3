from multiprocessing import Pool
import os,time,random
def long_time_task(name):
	print('启动任务 %s (%s)..' % (name,os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	#random()函数取得范围为[0,1]
	end = time.time()
	print('task %s runs %0.2f seconds.' % (name,(end - start)))

if __name__ == '__main__':
	print('Parent process %s' % os.getpid())
	p = Pool(4)
	for x in range(5):
		p.apply_async(long_time_task,args=(x,))
	print("Waiting for all subprocesses done...")
	p.close()
	p.join()
	print('All subprocesses done.')