def find(l, x):
	while(x != l[x]):
		x = l[x]
	return(x)

def unite(l, s, a, b):
	a = find(l, a)
	b = find(l, b)
	if(a == b):
		return
	if(s[a] < s[b]):
		a, b = b, a
	s[a] += s[b]
	l[b] = a

rows, columns = map(int, input().split())
l = [i for i in range(rows * columns)]
s = [1] * rows * columns
a = [None] * rows
for i in range(rows):
	a[i] = list(map(int, list(input())))

for i in range(0, rows):
	for j in range(0, columns):
		if(j < columns-1 and a[i][j] == a[i][j+1]):
			unite(l, s, i * columns + j, i * columns + j + 1)
		if(i < rows-1 and a[i][j] == a[i + 1][j]):
			unite(l, s, i * columns + j, (i + 1) * columns + j)
#print(l)
qs = int(input())
for _ in range(0, qs):
	r1, c1, r2, c2 = [int(x) - 1 for x in input().split()]
	#print()
	if(find(l, r1 * columns + c1) == find(l, r2 * columns + c2)):
		print('decimal' if a[r1][c1] else 'binary')
	else:
		print('neither')

