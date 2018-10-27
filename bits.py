cases = int(input())
for i in range(cases):
	inp = input()
	max_ = 0
	for j in range(1, len(inp)+1):
		num = int(inp[:j])
		#print(num)
		max_ = max(max_, bin(num).count("1"))
	print(max_)