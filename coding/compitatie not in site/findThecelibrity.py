# https://www.youtube.com/watch?v=LZJBZEnoYLQ&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=23
knownTable={
	0:{1,2,3}, 1:{0,2},2:set({}),3:{1,2}
}
def knows(i,j) -> bool:
	global knownTable
	return j in knownTable[i]

def findCelib(n=4) -> int:
	# 1st loop tells us a person who does not knows his <ahead> persons
	# may be he is a celib
	celib=0
	for i in range(1,n):
		if knows(celib,i):
			# he can not be a celib anymore as he knows someone <ahead>
			celib = i
	# confirming is he proper celib or not
	# my celib shoud be known to all and he knows none
	for i in range(n):
		if i!=celib and (knows(celib,i) or not knows(i,celib)):
			return -1
	return celib


if __name__ == '__main__':
	print(findCelib())