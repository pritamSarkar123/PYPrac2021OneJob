# https://www.youtube.com/watch?v=ED4ateJu86I&t=243s

from collections import OrderedDict
def create_range_dict(message):
	d = OrderedDict()
	for i in range(len(message)):
		c = message[i]
		if c not in d:
			d[c]=[i,i]
		else:
			d[c][-1]=i 
	return d

def make_partitions(message):
	range_dict = create_range_dict(message)
	partitions = OrderedDict()
	last_partition = None 
	for key in range_dict:
		if not last_partition:
			last_partition = key
			partitions[key] = range_dict[key] 
		else:
			current = range_dict[key]
			if current[0] > partitions[last_partition][-1]:
				last_partition = key
				partitions[key] = current.copy()
			else:
				partitions[last_partition] = [min(current[0],partitions[last_partition][0]),max(current[1],partitions[last_partition][1])] 
	
	ans = []
	for key in partitions:
		ans.append(partitions[key][-1] - partitions[key][0] + 1)
	return ans






message = "abacdefe"
part_list = make_partitions(message)
print(part_list)