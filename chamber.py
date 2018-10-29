edges, querues = map(int, input().split())
graph = {}


def bfs(target, graph):
	try:
		visited = []
		queue = [target]
		while(queue):
			node = queue.pop(0)
			#print("node")
			if node not in visited:
				visited.append(node)
				neighbors = graph[node]
				for neighbor in neighbors:
					queue.append(neighbor)
		return(visited)
	except KeyError:
		return(target)

for i in range(edges):
	#print(graph)
	x, y = input().split()
	if x in graph:
		graph[x].add(y)
	else:
		graph[x] = {y}
	if y not in graph:
		graph[y] = set({})
#print(graph)
for i in range(querues):
	#print(i)
	one, two = map(list, input().split())
	trans = True
	if(len(one) != len(two)):
		trans = False

	if(trans):
		for k in range(len(one)):
			if(two[k] in bfs(one[k], graph)):

				trans = True
			else:
				trans = False
				break

	if(trans):
		print("yes")
	else:
		print("no")