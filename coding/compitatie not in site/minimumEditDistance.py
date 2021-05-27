# https://www.youtube.com/watch?v=We3YDTzNXEk

# 2 strings given
# need to find min no of operations to convert one string to another
# operations be like replace, delete , add

# for simplicity make len(one) >len(two)

# we have to convert from one to two

one = "abcdeff"
two = "azpced"

table=[]
for _ in range(len(two)+1):
	table.append([0]*(len(one)+1))

changes = 0
for i in range(len(one)+1):
	table[0][i]=changes
	changes += 1

changes=0
for i in range(len(two)+1):
	table[i][0]=changes
	changes += 1

for i in range(1,len(two)+1):
	for j in range(1,len(one)+1):
		if one[j-1] == two[i-1]:
			table[i][j] = table[i-1][j-1]
		else:
			table[i][j] = min(table[i-1][j-1],table[i-1][j],table[i][j-1]) + 1

for _ in table:
	print(_)


i = len(table)-1
j = len(table[0])-1

while i!=0 and j!=0:
	if two[i-1] == one[j-1]:
		print(f"do nothing keep {one[j-1]} in one")
		i-=1;j-=1
	else:
		if table[i][j]==table[i-1][j-1]+1:
			# diag
			print(f"replace {one[j-1]} in one with {two[i-1]} of two")
			i-=1;j-=1
		elif table[i][j]==table[i-1][j]+1:
			# up
			print(f"add {two[i-1]} to one")
			i-=1
		elif table[i][j]==table[i][j-1]+1:
			# left
			print(f"delete one's {one[j-1]}")
			j-=1

# time =O(m*n)
# space =O(m*n)