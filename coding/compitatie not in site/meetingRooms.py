
# https://www.youtube.com/watch?v=i2bBG7CaVxs&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=26
from typing import List
def aPersonCanAttendAll(intervavls: List[int]) -> bool:
	intervavls.sort(key=lambda x:x[0])
	for i in range(1,len(intervavls)):
		if intervavls[i][0] < intervavls[i-1][1]:
			return False
	return True


if __name__ == '__main__':
	intervals1= [[0,30],[5,10],[15,20]]
	intervals2= [[7,10],[2,4]]
	print(aPersonCanAttendAll(intervals1))
	print(aPersonCanAttendAll(intervals2))