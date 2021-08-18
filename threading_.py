from threading import Thread,Lock,current_thread
import time
from queue import Queue

NO_OF_THREADES=21

def chatting(val):
	temp=5
	while temp:
		print(f"Busy in chatting {current_thread().name} val = {val}")
		time.sleep(0.5)
		temp-=1

def reconnect(val):
	temp=5
	while temp:
		print(f"reconnecting server {current_thread().name} val = {val}")
		time.sleep(0.5)
		temp-=1

def work(q):
	x=q.get()
	if (x&1)==1:
		chatting(x)
	else:	
		reconnect(x)
	q.task_done() #it ensured task of a thread complets here
	# it makes the queue thread safe 

if __name__ == "__main__":
	q=Queue()
	for _ in range(NO_OF_THREADES):
		t=Thread(target=work,args=(q,),daemon=True)
		t.start()

	for i in range(NO_OF_THREADES):
		q.put(i)
	q.join() # it ensures main thread will not be completed
	#untill all the elements in the queue aar dequeued and processed properly
