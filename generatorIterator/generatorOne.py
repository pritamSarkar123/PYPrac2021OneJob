def makeSquare(L):
	a=[]
	for i in L:
		a.append(i*i)
	return a


def makeSquareGeneratorOne(L):
	for i in L:
		yield i*i

if __name__ == '__main__':
	L=[1,2,3,4,5,6,7,8,9]
	print(makeSquare(L),type(makeSquare(L)))
	gen_square_one=makeSquareGeneratorOne(L)
	gen_square_two=makeSquareGeneratorOne(L)
	print(type(gen_square_one))
	# <class 'generator'>
	for i in range(len(L)):
		print(next(gen_square_one),end=" ")
	print()
	# 1 4 9 16 25 36 49 64 81 

	for square in gen_square_two:
		print(square, end=" ")
	print()
	# 1 4 9 16 25 36 49 64 81 

	my_square_maker=lambda l:(x*x for x in l)
	gen_square_three=my_square_maker(L)
	print(type(gen_square_three)) #<class 'generator'>

	for square in gen_square_three:
		print(square, end=" ")
	print()
	# 1 4 9 16 25 36 49 64 81 



