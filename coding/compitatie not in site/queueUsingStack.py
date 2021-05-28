class MyQueue:
	def __init__(self):
		self.stack = []
	def enque(self,val):
		self.stack.append(val)
	def deque_rec(self):
		if len(self.stack) ==0:
			return None
		return self.from_Stack()
	def deque_iter(self):
		if len(self.stack) ==0:
			return None
		return self.from_stack_iter()
	def from_stack_iter(self):
		result = None
		record_stack=[]
		while len(self.stack) !=1:
			record_stack.append(self.stack.pop())
		result = self.stack.pop()
		while len(record_stack):
			self.stack.append(record_stack.pop())
		return result

	def from_Stack(self):
		if len(self.stack) ==1:
			return self.stack.pop()
		temp = self.stack.pop()
		result = self.from_Stack()
		self.stack.append(temp)

		return result
	def __str__(self):
		return f"{self.stack}"


mq = MyQueue()
l = [1,2,3,4,5,6,7,8]

for i in l:
	mq.enque(i)
print(mq)

print(mq.deque_rec())
print(mq)

print(mq.deque_iter())
print(mq.deque_iter())
print(mq)


[1, 2, 3, 4, 5, 6, 7, 8]
1
[2, 3, 4, 5, 6, 7, 8]
2
3
[4, 5, 6, 7, 8]