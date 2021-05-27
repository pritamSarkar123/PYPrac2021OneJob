from collections import Counter

l1=[1,2,34,21,5,6,7,8,9,21,3,2,1,34]
t1=(1,2,34,21,5,6,7,8,9,21,3,2,1,34)

list_counter=Counter(l1)
touple_counter=Counter(t1)

print(list_counter)
print(touple_counter)
# Counter({1: 2, 2: 2, 34: 2, 21: 2, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 3: 1})
# Counter({1: 2, 2: 2, 34: 2, 21: 2, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 3: 1})

print(list_counter[34])
# 2
list_counter[34]=5
print(list_counter)
# Counter({34: 5, 1: 2, 2: 2, 21: 2, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 3: 1})

print(list(list_counter.elements()))
# [1, 1, 2, 2, 34, 34, 34, 34, 34, 21, 21, 5, 6, 7, 8, 9, 3]

print(list_counter.most_common())
print(list_counter.most_common()[0])
# [(34, 5), (1, 2), (2, 2), (21, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (3, 1)]
# (34, 5)
deduct = {34:3,1:2}
list_counter.subtract(deduct)
print(list_counter)
# Counter({2: 2, 34: 2, 21: 2, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 3: 1, 1: 0})
