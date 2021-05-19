import time
import random
import memory_profiler

# rom memory_profiler import memory_usage
# mem_usage = memory_usage(-1, interval=.2, timeout=1)
# -1 current process

def peopleList(num):
	p=[]
	for i in range(num):
		p.append(random.randint(i,i*100))
	return p

peopleGen=lambda num:(random.randint(i,i*100) for i in range(num))

def methOne():
	print(f"memory usage {memory_profiler.memory_usage()[0]} Mb before")
	start=time.time()
	p=peopleList(100000)
	print(f"time taken {time.time()-start} s")
	print(f"memory usage {memory_profiler.memory_usage()[0]} Mb after")

def methTwo():
	print(f"memory usage {memory_profiler.memory_usage()[0]} Mb before")
	start=time.time()
	p=peopleGen(100000)
	print(f"time taken {time.time()-start} s")
	print(f"memory usage {memory_profiler.memory_usage()[0]} Mb after")


if __name__ == '__main__':
	methOne()
	# memory usage 18.2265625 Mb before
	# time taken 0.2655632495880127 s
	# memory usage 22.875 Mb after
	methTwo()
	# memory usage 18.37109375 Mb before
	# time taken 0.0 s
	# memory usage 18.37109375 Mb after