# https://www.youtube.com/results?search_query=Find+The+Second+Largest+Item+-+Heap+%26+Tracking+Approach+(Beginner+Big+N+Interview+Question)

import heapq

def findSecondLargestUsingHeap(arr):
	my_heap=[]
	heapq.heapify(my_heap)

	max_length = 2
	current_length=0
	for num in arr:
		heapq.heappush(my_heap, num)
		current_length += 1
		if current_length > max_length:
			heapq.heappop(my_heap)
			current_length -=1
	print(my_heap)


def findKthLargestUsingHeap(arr,k):
	my_heap=[]
	heapq.heapify(my_heap)

	max_length = k
	current_length=0
	for num in arr:
		heapq.heappush(my_heap, num)
		current_length += 1
		if current_length > max_length:
			heapq.heappop(my_heap)
			current_length -=1
	print(my_heap)

def findKthDistinctLargestUsingHeap(arr,k):
	my_heap=[]
	heapq.heapify(my_heap)
	visited=set()
	max_length = k
	current_length=0
	for num in arr:
		if num not in visited:
			heapq.heappush(my_heap, num)
			visited.add(num)
			current_length += 1
		if current_length > max_length:
			heapq.heappop(my_heap)
			current_length -=1
	print(my_heap)



def findSecondLargestUsingPointers(arr):
	first = float('-inf')
	second = float('-inf')

	for num in arr:
		if num > first:
			second = first
			first = num
		else:
			if num != first and num > second:
				second = num

	print(first,second)





if __name__ == '__main__':
	arr=[-1,10,8,9,10,9,-8,11,15]
	findSecondLargestUsingHeap(arr)
	findKthLargestUsingHeap(arr,3)
	findKthLargestUsingHeap(arr,5)
	findKthDistinctLargestUsingHeap(arr,5)
	# all agos above takes O(n * log(k+1)) time and O(n) space
	findSecondLargestUsingPointers(arr) # this takes O(n) time and O(1) space
