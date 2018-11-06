grid = []
for i in range(0, 4):
	grid.append(list(input()))
	
def distance(place, letter):
	return(abs(pos[letter][0] - place[0]) + abs(pos[letter][1] - place[1]))

pos = {'A':(0,0), 'B':(0,1), 'C':(0,2), 'D':(0,3), 'E':(1,0), 'F':(1,1), 'G':(1,2), 'H':(1,3), 'I':(2,0), 'J':(2,1), 'K':(2,2), 'L':(2,3), 'M':(3,0), 'N':(3,1), 'O':(3,2)}

total = 0
for row in range(0, 4):
	for col in range(0, 4):
		if(grid[row][col] != "." and (row !=  pos[grid[row][col]][0]  or col !=  pos[grid[row][col]][1])):
			total += distance([row, col], grid[row][col])
print(total)