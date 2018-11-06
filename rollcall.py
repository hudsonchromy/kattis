import operator

names = []
firstNames = []
while True:
	try:
		newName = list(input().split())
		names.append(newName)
		firstNames.append(newName[0])
	except EOFError:
		break

names = sorted(names, key = operator.itemgetter(1,0))
for name in names:
	if(firstNames.count(name[0]) > 1):
		print(name[0] + " " + name[1])
	else:
		print(name[0])