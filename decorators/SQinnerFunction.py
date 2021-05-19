def make_inner_function(nums):
	def inner_function():
		l=[]
		for i in range(nums):
			l.append(i*i)
		return l
	return inner_function

get_squares=make_inner_function(10)
print(get_squares())

def inner_square(nums):
	l=[]
	for i in range(nums):
		l.append(i*i)
	return l
get_squares_using_lambda=lambda: inner_square(10)
print(get_squares_using_lambda())