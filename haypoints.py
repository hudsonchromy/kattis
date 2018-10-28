dictL, pays = map(int, input().split())
words = dict()
for _ in range(dictL):
	word, pay = input().split()
	words[word] = int(pay)

for _ in range(pays):
	para = []
	inp = input()
	while(inp != "."):
		para.extend(inp.split())
		inp = input()
	pay = 0
	for word in para:
		if(word in words):
			pay += words[word]
	print(pay)
