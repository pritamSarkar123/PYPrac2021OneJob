from collections import deque

l=[1,2,3,4,5,6,7,8,9]

d=deque(l)

d.append(15)
d.appendleft(10)
print(d)
# deque([10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15])

d.pop()
d.popleft()
print(d)
# deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(d.count(1))
# 1
d1=d.copy()
print(d1)
# deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

d1.clear()
print(d1)
# deque([])
