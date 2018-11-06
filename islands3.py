def neighbors(r, c, visited, graph):
	outp = []
	#print(visited)
	#print(graph[r][c+1])
	#print(graph[r-1][c] == "C" or graph[r-1][c] == "L")
	if(r-1 >= 0 and (graph[r-1][c] == "C" or graph[r-1][c] == "L") and visited[r-1][c] == False):
		outp.append([r-1, c])
	if(c-1 >= 0 and (graph[r][c-1] == "C" or graph[r][c-1] == "L") and visited[r][c-1] == False):
		outp.append([r, c-1])
	if(r + 1 < len(graph) and (graph[r+1][c] == "C" or graph[r+1][c] == "L") and visited[r+1][c] == False):
		outp.append([r+1, c])
	if(c + 1 < len(graph[0]) and (graph[r][c+1] == "C" or graph[r][c+1] == "L") and visited[r][c+1] == False):
		outp.append([r, c+1])
	return(outp)



def bfs(startR, startC, visited, graph):
	queue = [[startR, startC]]
	#print(queue)
	visited[startR][startC] = True
	while queue:
		#print(queue)
		node = queue.pop(0)
		#print("node", node)
		adj = neighbors(node[0], node[1], visited, graph)
		#print(adj)
		for place in adj:
			visited[place[0]][place[1]] = True
		queue.extend(adj)
	return(visited)


def main():
	islands = 0
	graph = []
	row, col = map(int, input().split())
	visited = [[False] * col for _ in range(row)]
	for _ in range(row):
		graph.append(list(input()))
	for r in range(0, row):
		for c in range(col):
			if(graph[r][c] == "L" and visited[r][c] == False):
				visited = bfs(r, c, visited, graph)
				islands += 1
	print(islands)


if __name__ == "__main__":
	main()