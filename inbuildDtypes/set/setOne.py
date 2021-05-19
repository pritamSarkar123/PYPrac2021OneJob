
s1={1,2,3}
s1.add(4)
print(s1)
# {1, 2, 3, 4}

s1={1,2,3}
s2={2,3,4}
# union & update 
u=s1.union(s2)
s1.update(s2)
print(u,s1)
# {1, 2, 3, 4} {1, 2, 3, 4}

s1={1,2,3}
s2={2,3,4}
# intersection and intersection_update
i=s1.intersection(s2)
s1.intersection_update(s2)
print(i,s1)
# {2, 3} {2, 3}

s1={1,2,3}
s2={2,3,4}
#difference and difference_update
d=s1.difference(s2)
s1.difference_update(s2)
print(d,s1)
# {1} {1}
s1={1,2,3}
s2={2,3,4}
d=s2.difference(s1)
s2.difference_update(s1)
print(d,s2)
# {4} {4}


s1={1,2,3}
s2={2,3,4}
sd=s1.symmetric_difference(s2)
s1.symmetric_difference_update(s2)
print(sd,s1)
# {1, 4} {1, 4}

s1={1,2,3}
s2={4,5,6}
print(s1.isdisjoint(s2))
# True

s1={1,2,3}
s2={1,2,3,4,5,6}
print(s1.issubset(s2))
# True
print(s2.issuperset(s1))
# True

s1={1,2,3,4,5,6}
try:
	s1.remove(9) # throws error
except KeyError:
	print(f"{9} not present")
finally:
	s1.remove(1)
	s1.discard(9) # not throw Error
	s1.discard(4)
print(s1)
# 9 not present
# {2, 3, 5, 6}

s1={1,2,3}
s1.clear()
print(s1)
# set()

s1={1,2,3}
s2=s1.copy()
print(id(s1),id(s2))
# 2166207216776 2166208319784


##### copy() methid is not available for tuple 
#### so we do
from copy import deepcopy
t1=(1,2,3,4,5)
t2=deepcopy(t1)
t3=t1[:]
t4=tuple(t1)
print(t1,t2,t3,t4)
print(id(t1),id(t2),id(t3),id(t4))
# (1, 2, 3, 4, 5) (1, 2, 3, 4, 5) (1, 2, 3, 4, 5) (1, 2, 3, 4, 5)
# 1809932998984 1809932998984 1809932998984 1809932998984
#  <- still providing same ref -_-

s1={"a":1, "b":2, "c":3}
s2=s1.copy()
s1["d"]=5
print(s1,s2)
# {'a': 1, 'b': 2, 'c': 3, 'd': 5} {'a': 1, 'b': 2, 'c': 3}