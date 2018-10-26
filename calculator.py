while True:
	try:
		inp = input()
		print('%.2f' % eval(inp))
	except EOFError:
		break