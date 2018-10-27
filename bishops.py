while True:
	try:
		inp = int(input())
		if(inp > 2):
			print(2 * inp - 2)
		else:
			print(inp)
	except EOFError:
		break