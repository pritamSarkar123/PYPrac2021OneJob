my_list=[
	[1,2,3],[4,5,6]
]
my_list_of_tuples=list(zip(*my_list))
my_list_of_lists=[list(x) for x in zip(*my_list)]
print(my_list_of_tuples)
print(my_list_of_lists)
# [(1, 4), (2, 5), (3, 6)]
# [[1, 4], [2, 5], [3, 6]]