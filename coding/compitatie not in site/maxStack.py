# https://www.youtube.com/watch?v=nGwn8_-6e7w

# giving max in O(1) time 
class MyStackApi:
	def __init__(self):
		self.stack = []
		self.cache = []
		self.cache_count = {}
		self.max_val = float("-inf")
	def update_cache(self,val=None,insert=False):
		if insert:
			if val > self.max_val:
				self.max_val = val
				if len(self.cache) == 0 or self.cache[-1] != val:
					self.cache.append(val)
					self.cache_count[val]=1
				else:
					self.cache_count[val]+=1

		else:
			if val == self.cache[-1]:
				self.cache_count[val]-=1
				if self.cache_count[val]==0:
					self.cache_count.pop(val)
					self.cache.pop()
					self.max_val = self.cache[-1]


	def push(self,val):
		self.stack.append(val)
		self.update_cache(val,True)

	def pop(self):
		popped_val=self.stack.pop()
		self.update_cache(popped_val)

	def get_max(self):
		return self.max_val

	def __str__(self):
		return f"{self.max_val}  {self.stack} {self.cache} {self.cache_count}"

m = MyStackApi()
l =[2,2,1,4,5,5,3]
for i in l:
	m.push(i)
print(m)
# 5  [2, 2, 1, 4, 5, 5, 3] [2, 4, 5] {2: 1, 4: 1, 5: 1}
for i in range(3):
	m.pop()
	print(m)
# 5  [2, 2, 1, 4, 5, 5] [2, 4, 5] {2: 1, 4: 1, 5: 1}
# 4  [2, 2, 1, 4, 5] [2, 4] {2: 1, 4: 1}
# 4  [2, 2, 1, 4] [2, 4] {2: 1, 4: 1}