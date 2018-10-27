range_ = [0, 1001]
times = []
through = True
cases = int(input())
for _ in range(cases):
	times.append(list(map(int, input().split())))
for lis in times:
	range_[0] = max(range_[0], lis[0])
	range_[1] = min(range_[1], lis[1])
if(range_[0] <= range_[1]):
	print("gunilla has a point")
else:
	print("edward is right")