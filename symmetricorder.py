case = 1
namesNum = int(input())
string = []
while(namesNum != 0):
	names = []
	string.append("SET " + str(case))
	string.append("\n")
	for _ in range(namesNum):
		names.append(input())
	for i in range(0, namesNum, 2):
		string.append(names[i])
		string.append("\n")
	#string.append("helf")
	if(namesNum & 1):
		for j in range(namesNum-2, 0, -2):
			string.append(names[j])
			string.append("\n")
	else:
		for j in range(namesNum-1, 0, -2):
			string.append(names[j])
			string.append("\n")
	case += 1
	namesNum = int(input())
print("".join(string[:-1]))