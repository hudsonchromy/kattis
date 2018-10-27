tree_num = int(input())
trees = sorted(list(map(int, input().split())), reverse = True)
trees.insert(0,0)
most = 0
for i in range(1, tree_num+1):
	most = max(most, (trees[i] + i))
	# print(most)
print(most + 1)