cases = int(input())
for _ in range(cases):
	inp = int(input())
	if(inp & 1):
		print(str(inp), " is odd")
	else:
		print(str(inp), " is even")
