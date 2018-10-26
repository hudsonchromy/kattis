#
#  N(0)
#W(3) E(1)
#  S(2)
#
facing_dict = {'F':0, 'B':2, 'R':1, 'L':3}
cases = int(input())
print(cases)
for i in range(cases):
	moves = list(input())
	#print(moves)
	max_rows = 0
	max_cols = 0
	curr_row = 0
	curr_col = 0
	start = 0
	facing = 1
	for move in moves:
		facing = (facing + facing_dict[move]) % 4
		if(facing == 1):
			max_cols = max_cols + 1 if max_cols == curr_col else max_cols
			curr_col += 1
		elif(facing == 0):
			at = max_rows
			max_rows = max_rows + 1 if curr_row == 0 else max_rows
			curr_row = curr_row - 1 if curr_row != 0 else 0
			start = start + 1 if at != max_rows else start
		elif(facing == 2):
			max_rows = max_rows + 1 if curr_row == max_rows else max_rows
			curr_row += 1
		else:
			max_cols = max_cols + 1 if curr_col == 0 else max_cols
			curr_col = curr_col - 1 if curr_col != 0 else 0
	facing = 1
	curr_row = start + 1
	curr_col = 0
	#print(start)
	matrix = [['#' for y in range(max_cols+2)] for x in range(max_rows+3)]

	for move in moves:
		facing = (facing + facing_dict[move]) % 4

		if(facing == 1):
			curr_col += 1
		elif(facing == 0):
			curr_row -=  1 
		elif(facing == 2):
			curr_row += 1
		else:
			curr_col -= 1
		#print(curr_col)
		#print(curr_row)
		matrix[curr_row][curr_col] = '.'

	print("{} {}".format(max_rows+3, max_cols+2))
	
	for y in range(max_rows+3):
		print("".join(matrix[y]))
