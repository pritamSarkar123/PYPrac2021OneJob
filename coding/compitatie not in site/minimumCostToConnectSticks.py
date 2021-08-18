# https://www.youtube.com/watch?v=3dqR2nYElyw&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=98
import heapq
def min_cost(sticks):
	total = 0
	heapq.heapify(sticks)
	while len(sticks) > 1:
		one = heapq.heappop(sticks)
		two = heapq.heappop(sticks)
		total += (one + two)
		heapq.heappush(sticks,(one + two))
	return total



if __name__== '__main__':
	sticks = [1,8,3,5]
	print(min_cost(sticks))