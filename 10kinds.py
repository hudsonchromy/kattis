ysize, xsize = map(int, input().split())
graphIn = []
for i in range(0, ysize):
	graphIn.append(list(input()))
graph = dict({})
for y in range(0, ysize):
	for x in range(0, xsize):
		edges = set()
		#print('here')
		if(y-1 >= 0 and graphIn[y][x] == graphIn[y-1][x]):
			edges.add((y-1, x))
		if(y+1 < ysize and graphIn[y][x] == graphIn[y+1][x]):
			edges.add((y+1, x))
		if(x-1 >= 0 and graphIn[y][x] == graphIn[y][x-1]):
			edges.add((y, x-1))
		if(x+1 < xsize and graphIn[y][x] == graphIn[y][x+1]):
			edges.add((y, x+1))
		graph[(y,x)] = edges

def dfs(graph, start, looking):
	if(looking not in graph or start not in graph):
		return False
	if(start == looking):
		return True
	visited, stack = set(), [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			if(vertex == looking):
				return True
			visited.add(vertex)
			#print(graph[vertex])
			#print(visited)
			stack.extend(graph[vertex] - visited)
	return False

cases = int(input())
for i in range(0, cases):
	y1, x1, y2, x2 = map(int, input().split())
	booling = dfs(graph, (y1-1, x1-1), (y2-1, x2-1))
	if(booling == False):
		print("neither")
	elif(graphIn[y1-1][x1-1] == '1'):
		print("decimal")
	else:
		print("binary")