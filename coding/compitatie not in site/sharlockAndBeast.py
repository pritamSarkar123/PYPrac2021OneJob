# https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def func(n:int):
	if n<=2:
		return "-1"

	if n%3==0:
		num =""
		while n:
			num +="5"
			n-=1
		return num

	f = 3
	t = -1
	min_t = float("inf")
	found =False
	while f <= n:
		t = n - f
		if t % 5 == 0:
			if t < min_t:
				min_t = t
			found = True
		f+=3
	max_f = n - min_t
	
	if not found:
		num =""
		if n%5 ==0:
			while n:
				num+="3"
				n-=1
			return num
		else:
			return "-1"
	else:
		num = ""
		while max_f:
			num+="5"
			max_f-=1

		while min_t:
			num+="3"
			min_t-=1
		return num


# d ={}
# for i in range(15):
# 	d[i]=func(i)
# print(d)
l=[69835,97167,9909,14953,81707,9283,66850,98100,50170,4317,65154,68262,42750,98509,46974,98203,6181,34738,1795,78539]
d ={}
for i in l:
	d[i]=func(i)

print(d)