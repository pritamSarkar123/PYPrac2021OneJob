import functools
# the function trys to arrange the list in such a way that
# the list gives the largest number formed using it
def my_number_compare(a,b):
	ab=a+b
	ba=b+a
	return 1 if ba > ab else -1 if ab > ba else 0

num_list = ["10","20","30","49","409","36"]

num_list.sort(key=functools.cmp_to_key(my_number_compare))
print(num_list)