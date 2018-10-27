cases = int(input())
for _ in range(cases):
	input()
	garmy = []
	marmy = []
	ng, nm = map(int, input().split())
	garmy = list(map(int, input().split()))
	marmy = list(map(int, input().split()))
	garmy.sort()
	marmy.sort()
	while(len(marmy) != 0 and len(garmy) != 0):
		if(garmy[0] >= marmy[0]):
			marmy.pop(0)
		else:
			garmy.pop(0)
	if(len(garmy) == 0):
		print("MechaGodzilla")
	else:
		print("Godzilla")
