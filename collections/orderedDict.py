from collections import OrderedDict,Counter

l1=[1,2,34,21,5,6,7,8,9,21,3,2,1,34]

c_l1=Counter(l1)

od_l1=OrderedDict(c_l1.most_common())

print(od_l1)
# OrderedDict([(1, 2), (2, 2), (34, 2), (21, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (3, 1)])

for key,value in od_l1.items():
	print(key,value)

# 1 2
# 2 2
# 34 2
# 21 2
# 5 1
# 6 1
# 7 1
# 8 1
# 9 1
# 3 1
# ordered dictionary maintains its insertion order

original_dict = dict(od_l1)
print(original_dict)
# {1: 2, 2: 2, 34: 2, 21: 2, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 3: 1}