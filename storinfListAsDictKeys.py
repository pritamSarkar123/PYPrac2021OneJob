# You don't have to implement __eq__() method for the hash as it is created by default for all objects.

my_list=[[1,2,3],[4,5,6],[7,8,9]]

sums={}

for ml in my_list:
	sums[tuple(ml)]=sum(ml)

print(sums)
