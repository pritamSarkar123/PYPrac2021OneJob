# https://www.youtube.com/watch?v=evesA3gr9BE&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=112
def find_shortest_way_to_form(source,target):
	number_of_sq = 0 
	remaining = target
	while remaining: 
		sq = ""
		i = 0
		j = 0
		while i < len(source) and j < len(remaining):
			if source[i] == remaining[j]:
				sq += source[i]
				j += 1
			i += 1
		if not sq:
			return -1

		number_of_sq += 1
		remaining = remaining[len(sq):]

	return number_of_sq




if __name__=="__main__":
	print(find_shortest_way_to_form("xyz","xzyxz"))