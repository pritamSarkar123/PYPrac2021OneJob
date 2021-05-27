# https://www.youtube.com/watch?v=E-kjYOZEBxY&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=27
from collections import deque
class MovingAverage:
	def __init__(self,window_size=3):
		self.window_size = window_size
		self.window=deque()
	def next(self,number: int) -> int:
		self.window.append(number)
		if len(self.window) > self.window_size:
			self.window.popleft()
		total=sum(self.window)
		count=len(self.window)
		return total//count

if __name__ =="__main__":
	ma = MovingAverage(3)
	l=[1,10,3,5]
	for _ in l:
		print(ma.next(_))
	
import os
print(os.listdir())