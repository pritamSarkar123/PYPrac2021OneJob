# https://www.youtube.com/watch?v=EvShMOf5CRQ

# creating the graph first
no_of_nodes = 7
graph = dict.fromkeys(range(no_of_nodes+1),None)
nodes =[[1,2],[0,3],[0,3,6,7],[1,2,4,5],[3,5],[3,4],[2,7],[2,6]]
for i in range(no_of_nodes+1):
	graph[i]=set(nodes[i])

print(graph)
# {0: {1, 2}, 1: {0, 3}, 2: {0, 3, 6, 7}, 3: {1, 2, 4, 5}, 4: {3, 5}, 5: {3, 4}, 6: {2, 7}, 7: {2, 6}}
# making the dfs and gathering actual edges
actual_edges = dict.fromkeys(range(no_of_nodes+1),None)
distances = dict.fromkeys(range(no_of_nodes+1),None)
stack = []
visited = set()
root = 0
stack.append(root) # 0 will be the starting node as an example
visited.add(root)
d=1
while len(stack):
	n = stack.pop()
	distances[n]=d
	for i in graph[n]:
		if i not in visited:
			visited.add(i)
			stack.append(i)
	if actual_edges[n] is None:
		actual_edges[n]=set()
	if len(stack):
		actual_edges[n].add(stack[-1])
	d+=1
for i in actual_edges.keys():
	if actual_edges[i] is None:
		actual_edges[i]=set()

print(actual_edges)
# {0: {1, 2}, 1: set(), 2: {3, 6, 7}, 3: {4, 5}, 4: set(), 5: set(), 6: set(), 7: set()}

# finding out the back edges
back_edges = dict.fromkeys(range(no_of_nodes+1),None)

for node in graph.keys():
	current = graph[node].difference(actual_edges[node])
	for _ in current:
		if node not in actual_edges[_]:
			if back_edges[node] is None:
				back_edges[node] =set()
			back_edges[node].add(_)

for i in back_edges.keys():
	if back_edges[i] is None:
		back_edges[i]=set()

print(f"back_edges : {back_edges}")

# finding out the lows

lows = dict.fromkeys(range(no_of_nodes+1),None)
for n in range(no_of_nodes+1):
	dfn = distances[n]

	min_child = float("inf")
	for c in actual_edges[n]:
		if distances[c] > distances[n]:
			if distances[c] < min_child:
				min_child = distances[c]

	min_back = float("inf")
	for b in back_edges[n]:
		if distances[b] < min_back:
			min_back = distances[b]

	lows[n] = min(dfn,min_child,min_back)

print(f"low s {lows}")
print(f"dfn s {distances}")
# {0: 1, 1: 5, 2: 2, 3: 5, 4: 6, 5: 6, 6: 3, 7: 3}
# {0: 1, 1: 8, 2: 2, 3: 5, 4: 7, 5: 6, 6: 4, 7: 3}

articulation_points =set()

for u in range(no_of_nodes+1):
	if u != root and len(actual_edges[u])!=0:
		for v in actual_edges[u]:
			if distances[u] <= lows[v]:
				articulation_points.add(u)
if len(actual_edges[root])>1:
	articulation_points.add(root)
print(f"articulation points :- {articulation_points}")
