import math

def func(d,nums,level=0,ans=[]):
	if level == len(d):
		nums.append(int("".join(ans)))
		return
	for i in range(len(d[level])):
		ans.append(d[level][i])
		func(d,nums,level+1,ans)
		ans.pop()


def findKthLargest(s,x,k):
	s1=" "+s
	no_of_steps = math.ceil(len(s)/x)
	d=[]
	for i in range(1,no_of_steps+1):
		j=((i-1)*x + 1)
		k=min(len(s), j+x-1)
		d.append(s1[j:k+1])

	nums=[]
	func(d,nums)

	nums.sort()
	return nums[k]


s="123456789912"
x=3
k=7
print(findKthLargest(s,x,k))