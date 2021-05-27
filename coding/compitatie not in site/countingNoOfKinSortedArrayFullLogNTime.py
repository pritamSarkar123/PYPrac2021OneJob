
def get_right_range(arr,k):
	l = 0
	r = len(arr)-1
	while l <= r:
		mid = l + (r - l) //2
		if arr[mid] == k:
			if mid + 1 < len(arr):
				if arr[mid] != arr[mid+1]:
					return mid
				else:
					l = mid + 1
			else:
				return mid
		elif arr[mid] < k:
			l = mid +1
		else:
			r = mid -1
	return -1

def get_left_range(arr,k):
	l=0
	r=len(arr)-1
	while l <= r:
		mid = l + (r - l) //2
		if arr[mid] == k:
			if mid -1 > -1:
				if arr[mid-1]!=arr[mid]:
					return mid
				else:
					r = mid -1
			else:
				return mid
		elif arr[mid] < k:
			 l = mid +1
		else:
			r = mid +1
	return -1
arr = [0,1,1,1,2,2,4,5]
k = 1
r = get_right_range(arr,1)
l = get_left_range(arr,1)
print(f"no of {k} is {r-l+1}")