# iterable :- the object which can be loopee over
# contains __iter__ method which returns the iterator
# but doesnot contains __next__ method 
l1=[1,2,3,4,54,6,76,7,8]
print('__iter__' in dir(l1))
print('__next__' in dir(l1))
# True
# False

# iterator :- the object which can remember its state during looping
# contains __iter__ method which returns its self reference
# contains __next__ method which returns the next element
itOne=l1.__iter__()
itTwo=iter(l1)
print(type(itOne),type(itTwo))
print(itOne==itTwo)
# <class 'list_iterator'> <class 'list_iterator'>
# False

nums=l1.copy() # nums=l1[:]

for num in nums:
	print(num,end=" ")
print()
# 1 2 3 4 54 6 76 7 8 

# what is going on inside?
it_num=iter(nums)
while True:
	try:
		print(next(it_num),end=" ")
	except StopIteration:
		break
print()
# 1 2 3 4 54 6 76 7 8 
