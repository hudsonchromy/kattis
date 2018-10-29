cases = int(input())
books = []

for _ in range(cases):
	books.append(int(input()))
books.sort(reverse = True)
dec = 0
for i in range(2, len(books), 3):
	books.pop(i - dec)
	dec += 1
print(sum(books))