
def lenOfNonDecSequences(arr):
	table =[1]*len(arr)
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if arr[j] >= arr[i]:
				table[j] = max(table[j], table[i]+1) # each time adding one new element
	print(table[-1]) 

def nonDecSequences(arr):
	table=[]
	for i in range(len(arr)):
		table.append([arr[i]])

	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if arr[j] >= arr[i]:
				old_len = len(table[j])
				new_len = len(table[i])+1
				if new_len > old_len:
					new_tab= table[i].copy()
					new_tab.append(arr[j])
					table[j]=new_tab.copy()

	print(table[-1])






if __name__ == '__main__':
	arr=[-1,3,4,5,2,2,2,2]
	lenOfNonDecSequences(arr)
	nonDecSequences(arr)