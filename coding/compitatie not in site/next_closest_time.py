# https://www.youtube.com/watch?v=99Gw7Hezii8&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=62

def create_digit_set(time):
	time_set = set()
	hour = []
	minute = []
	minute_turn = False
	for c in time:
		if c.isnumeric():
			num = int(c)
			time_set.add(num)
			if minute_turn:
				minute.append(num)
			else:
				hour.append(num)
		else:
			minute_turn =True

	return time_set,hour[0]*10+hour[1],minute[0]*10+minute[1]

def digit_count(num):
	if num == 0:
		return 1
	count = 0
	while num:
		count+=1
		num//=10
	return count

def in_string(current_hour,current_min):
	str_current_hour =""
	str_current_min = ""

	if digit_count(current_min) == 1:
		str_current_min = "0"+str(current_min)
	else:
		str_current_min = str(current_min)

	if digit_count(current_hour) == 1:
		str_current_hour = "0"+str(current_hour)
	else:
		str_current_hour = str(current_hour)

	return str_current_hour+":"+str_current_min

# space O(16)
# time O(16 + n)
def find(time_set,hour,minute):
	str_current_hour=""
	str_current_min=""
	time_list = list(time_set)
	pairs = []
	for i in time_list:
		for j in time_list:
			num = i*10+j
			if num < 60:
				pairs.append(num)
	pairs = set(pairs)

	current_min = minute
	
	carry = 0
	# set minute 1st 
	while True:
		current_min += 1 
		if current_min >= 60:
			current_min = 0
			carry = 1
		if current_min in pairs:
			break

	current_hour = hour 

	if not carry:
		return in_string(current_hour,current_min)

	while True:
		current_hour += 1 
		if current_hour >= 24:
			current_hour = 0
		if current_hour in pairs:
			break
	return in_string(current_hour,current_min)


times = ["08:49","23:59","19:39","19:34","06:30",]
for time in times:
	time_set,hour,minute = create_digit_set(time)
	print(find(time_set,hour,minute))
	# break