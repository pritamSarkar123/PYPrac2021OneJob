class MyRange():
	def __init__(self,*args):
		if len(args)>0 and any(not isinstance(arg,int) for arg in args):
			raise TypeError

		self.reverse=False
		if len(args)==1:
			self.start,self.end,self.step=0,args[-1],1
		elif len(args)==2:
			self.start,self.end,self.step=args[0],args[-1],1
		elif len(args)==3:
			self.start,self.end,self.step=args[0],args[1],args[-1]
		else:
			raise ValueError

		if self.step<0:
			self.reverse=True

	def __iter__(self):
		return self

	def __next__(self):
		if (not self.reverse and self.start>=self.end) or (self.reverse and self.start<=self.end):
			raise StopIteration
		current=self.start
		self.start+=self.step
		return current

if __name__ == "__main__":
	for i in MyRange(1,11,2):
		print(i,end=" ")
	print()
	# 1 3 5 7 9 
	it=iter(MyRange(1,11,2))
	while True:
		try:
			print(next(it),end=" ")
		except StopIteration:
			break
	print()
	# 1 3 5 7 9 
	print(type(MyRange(1,11,2)))
	# <class '__main__.MyRange'>
