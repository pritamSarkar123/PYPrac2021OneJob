import heapq
class MyHeap:
	def __init__(self,items=None,key=lambda x:x):
		self.__heap_list=items
		self.__heap_key = key
		self.__heap_index = 0

		if items:
			self.__heap_list = [(self.__heap_key(item),i,item) for i,item in enumerate(items)]
			self.__heap_index = len(self.__heap_list)
			heapq.heapify(self.__heap_list)
		else:
			self.__heap_list = []
	
	def push(self,item):
		heapq.heappush(self.__heap_list,(self.__heap_key(item),self.__heap_index,item))
		self.__heap_index += 1

	def pop(self):
		return heapq.heappop(self.__heap_list)

	def show(self):
		print(self.__heap_list)

	def __repr__(self):
		return f"{len(self.__heap_list)}"


if __name__ == '__main__':
	l =[[0,30],[15,20],[5,10]]
	heap = MyHeap(l,key = lambda x:-x[0])
	print(type(heap),heap)
	heap.show()

