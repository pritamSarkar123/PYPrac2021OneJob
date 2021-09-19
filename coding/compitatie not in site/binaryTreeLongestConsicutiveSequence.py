# https://www.youtube.com/watch?v=oSYGjIq6ZM4&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=114



###
# need to create a binary tree first
###

def findLongestSeq(root) -> int:
	m = [0]
	func(root,0,0,m)
	return m[0]

def func(root,count,target,m):
	if not root:
		return 
	elif root.val == target.val:
		count += 1
	else:
		count = 1
	m[0] = max(m[0],count)
	func(root.left,count,root.val+1,m)
	func(root.right,count,root.val+1,m)


if __name__=="__main__":
	# incomplete