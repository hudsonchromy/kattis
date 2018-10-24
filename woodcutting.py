#woodcutting.py
cases = int(input())
for i in range(cases):
	customers = int(input())
	q = [0]
	for j in range(customers):
		cut = 0
		pieces = list(map(int, input().split()))
		for k in range(1, len(pieces)):
			cut += pieces[k]
		q.append(cut)

	q.sort()
	wait = 0
	#print(pieces)
	for l in range(1, len(q)):
		wait += q[l] * (customers - l + 1)
	#print(q)
	res = wait / customers
	print(res)