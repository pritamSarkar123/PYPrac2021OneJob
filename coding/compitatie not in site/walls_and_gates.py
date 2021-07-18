# https://www.youtube.com/watch?v=Pj9378ZsCh4&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=72
# 99 empty room, -1 wall, 0 gate
grid = [
	[99,-1,0,99],
	[99,99,99,-1],
	[99,-1,99,-1],
	[0,-1,99,99]
]

def fillup(i,j,count):
	global grid
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] < count:
		return
	grid[i][j] = min(grid[i][j],count)
	fillup(i+1,j,count+1)
	fillup(i-1,j,count+1)
	fillup(i,j+1,count+1)
	fillup(i,j-1,count+1)

for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == 0:
			fillup(i,j,0)

print(*grid,sep="\n")




