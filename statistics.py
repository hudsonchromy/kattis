#statistics.py
case = 1
while True:
	try:
		inp = list(map(int, input().split()))[1:]
		most = max(inp)
		least = min(inp)
		print("Case", str(case) + ":", str(least), str(most), str(most-least))
		case += 1
	except EOFError:
		break