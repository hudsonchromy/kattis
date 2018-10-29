while True:
	try:
		inp = list(map(int, input().split()))
		n = inp[0]
		L = inp[1:]
		if(n == 1):
			print("Jolly")
			continue
		set_nums = set()
		jolly = True
		for i in range(1, n):
			set_nums.add(abs(L[i] - L[i-1]))

		comp = set(range(1, n))

		if comp and set_nums == comp:
			jolly = True
		else:
			jolly = False
			# for i in range(0, n-1):
			# 	diff = abs(L[i] - L[i+1])
			# 	if( diff in set_diff):
			# 		set_diff.remove(diff)
			# 	else:
			# 		break
		if not jolly:
			print("Not Jolly")
		else:
			print("Jolly")
	except EOFError:
		break