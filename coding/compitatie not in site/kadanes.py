
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





arr =[-5,4,6,-3,4,-1]
# arr= [9,-9,5]
# arr =[2,-15,12]
# arr =[6,-9,-10]
print(max_sum_subarray(arr))
# (2, 4, 6)