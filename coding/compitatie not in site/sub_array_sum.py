# https://www.youtube.com/watch?v=XzwUBIkR9pA&t=398s
def find_all_subarrays(arr,target):
	d = {}
	ans = []
	start = 0
	end = -1
	cur_sum = 0
	for i in range(len(arr)):
		cur_sum += arr[i]
		if cur_sum - target ==0:
			end = i
			ans.append(arr[0:end+1])
		elif cur_sum - target in d:
			start = d[cur_sum - target] + 1
			end = i 
			ans.append(arr[start:end+1])
		d[cur_sum]=i
	return ans

def find_eq_0_1(arr):
	# needed to be debugged
	target = 0
	temp = arr.copy()
	for i in range(len(arr)):
		if not arr[i]:
			arr[i]=-1
	d = {}
	ans = []
	start = 0
	end = -1
	cur_sum = 0
	for i in range(len(arr)):
		cur_sum += arr[i]
		if cur_sum - target ==0:
			end = i
			ans.append([0,end])
		elif cur_sum - target in d:
			start = d[cur_sum - target] + 1
			end = i 
			ans.append([start,end])
		d[cur_sum]=i
	return ans

arr = [10,15,-5,10,5,15,-10,5,35,-25]
target = 5
print(find_all_subarrays(arr,target))
print(find_eq_0_1([1,0,1,1,0,1,1,0,0]))
