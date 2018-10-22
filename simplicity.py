import operator
inp = list(input())
value = len(set(inp))
vals = []
done = []
index = {}
ind = 0
for let in inp:
	if(let not in done):
		done.append(let)
		vals.append([let, 1])
		index[let] = ind
		ind += 1
	else:
		vals[index[let]][1] += 1
vals = sorted(vals, key=operator.itemgetter(1))
k = 0
dele = 0
while(value > 2):
	value -= 1
	dele += vals[k][1]
	k += 1

print(dele)