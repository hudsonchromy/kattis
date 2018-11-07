cases = int(input())
for _ in range(cases):
	first = list(input())
	second = list(input())
	diffs = []
	for i in range(len(first)):
		if(first[i] == second[i]):
			diffs.append(".")
		else:
			diffs.append("*")
	print("".join(first))
	print("".join(second))
	print("".join(diffs))
	print("\n")