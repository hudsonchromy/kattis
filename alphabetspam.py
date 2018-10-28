#alphabetspam.py
inp = list(input())
#whitespace - lowercase - uppercase - symbols
#print(inp)
count = [0,0,0,0]
for ch in inp:
	if(ch == "_"):
		count[0] += 1
	elif(ord(ch) >= 97 and ord(ch) <= 122):
		count[1] += 1
	elif(ord(ch) >= 65 and ord(ch) <= 90):
		count[2] += 1
	else:
		#print(ch)
		count[3] += 1
for coun in count:
	print(coun/len(inp))