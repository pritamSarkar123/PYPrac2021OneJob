# https://www.youtube.com/watch?v=VNbkzsnllsU
# hights = [3,2,1,0,4,5,6,0,2]
# hights=[2,4]
hights=[4,2,0,3,2,5]

max_area = float("-inf")

starting_pos =[]
current_hight = []

i =0 
while i < len(hights):
	if not len(current_hight):
		# if both stacks are empty insert it
		starting_pos.append(i)
		current_hight.append(hights[i])

	elif hights[i] > current_hight[-1]:
		# if stack is not empty and incomming hight is greater than the top(current_hight)
		starting_pos.append(i)
		current_hight.append(hights[i])

	else:
		print(hights[i],current_hight[-1])
		while len(current_hight) and hights[i] < current_hight[-1]:
			current_area = current_hight[-1] * (i - starting_pos[-1])
			current_hight.pop() # pop out the topmost hight
			if len(current_hight) and hights[i] <= current_hight[-1]: # if still the topmost hight > incomming hight
				starting_pos.pop()
			if current_area > max_area:
				max_area = current_area
		# finally push the hight and the position
		if not len(current_hight) or current_hight[-1] != hights[i]:
			current_hight.append(hights[i])
	i+=1

print(starting_pos)
print(current_hight)
print(i)
while len(current_hight):
	current_area = current_hight[-1] * (i - starting_pos[-1])
	current_hight.pop()
	starting_pos.pop()
	if current_area > max_area:
		max_area = current_area

print(max_area)

