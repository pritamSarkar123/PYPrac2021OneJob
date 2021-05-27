one = "abcdef"
two = "acbcf"

table = []
for i in range(len(two)+1):
	table.append([0]*(len(one)+1))

for i in range(1,len(two)+1):
	for j in range(1,len(one)+1):
		if one[j-1] == two[i -1]:
			table[i][j]= table[i-1][j-1] + 1 # another match found
		else:
			table[i][j]= max(table[i-1][j],table[i][j-1])


print(f"lasgest common subsequence of size {table[-1][-1]}")

i =  len(table)-1 # for two
j = len(table[0]) -1 #for one
common = []
while i>0 and j>0:
	if two[i-1] == one[j-1]:
		common.insert(0,one[j-1])
		i-=1;j-=1
	elif table[i][j] == table[i-1][j]:
		i-=1
	else:
		j-=1

print("".join(common))
