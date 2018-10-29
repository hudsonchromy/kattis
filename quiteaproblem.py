while True:
	try:
		inp = input()
		if("problem" in inp.lower()):
			out = ("yes")
		else:
			out = ("no")
		print(out)
	except EOFError:
		break