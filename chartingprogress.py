file = [[]]
i = 0
while True:
	try:
		inp = input()
		if(inp == ''):
			i += 1
			file.append([])
		else:
			file[i].append(list(inp)) 
	except EOFError:
		break
#print(i)
for j in range(0, i+1):
	#print("j")
	row_count = [0 for y in range(len(file[j]))]
	#print(row_count)
	for k in range(len(file[j])):
		row_count[k] = file[j][k].count('*')
	file[j] = [['.'for y in range(len(file[j][0]))] for x in range(len(file[j]))] 
	col = 0
	for k in range(len(file[j]) - 1, -1, -1):
		for _ in range(row_count[k]):
			file[j][k][col] = '*'
			col += 1
	#print(file[j])

	for l in range(len(file[j])):
		#print("h")
		print("".join(file[j][l]))
	if(j != i):
		print()
