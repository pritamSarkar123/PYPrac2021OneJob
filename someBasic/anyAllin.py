l1=range(0,11,2)
l2=list(map(lambda x: (x&1)==0,l1))
print(l2)
print(any(l2)) # True if any one element in the iterable is True
print(all(l2)) # True if all elements in the iterable is True

print(any([True,True,False]))
print(all([True,True,False]))
# True
# False