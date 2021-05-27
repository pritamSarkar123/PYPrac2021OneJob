# https://www.youtube.com/watch?v=yCQN096CwWM
def max_sum_subarray(arr):
	max_sum = float("-inf")
	current_sum = 0
	for i in range(len(arr)):
		current_sum += arr[i]

		if current_sum > max_sum:
			max_sum = current_sum
			end = i
		if current_sum <0:
			current_sum = 0

	start=end
	current_sum = max_sum
	while current_sum and start > -1:
		current_sum -= arr[start]
		start -= 1
	start += 1
	return (start,end,max_sum)

def find_largest_sum_rectangle(arr):
	max_sum = float("-inf")
	max_left,max_right,max_top,max_buttom = 0,0,0,0
	right =0 
	for left in range(len(arr[0])):
		aux_arr = [0]* len(arr)
		for right in range(left,len(arr[0])):
			for i in range(len(arr)):
				aux_arr[i] += arr[i][right]
			current_top,current_buttom,current_sum = max_sum_subarray(aux_arr)
			if current_sum > max_sum:
				max_sum = current_sum
				max_left = left
				max_right = right
				max_top = current_top
				max_buttom = current_buttom
	return (max_top,max_buttom,max_left,max_right)


arr =[
	[6,5,-7],[-9,3,-6],[-10,4,7]
]
t,b,l,r=find_largest_sum_rectangle(arr)

print(t,b,l,r)

for i in range(t,b+1):
	for j in range(l,r+1):
		print(arr[i][j],end= " ")
	print()

# time O(n^3)