cases = int(input())
for i in range(0, cases):
	s, d = map(int, input().split())
	if((s+d) % 2 == 1 or s < d):
		print("impossible")
	else:
		scoreW = (s+d)//2
		scoreL = s - scoreW
		print("{} {}".format(scoreW, scoreL))