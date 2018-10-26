cases = int(input())
outp = []
for _ in range(cases):
	inp = input()
	if(inp[:10] == "Simon says"):
		outp.append(inp[11:])
		outp.append("\n")
print("".join(outp[:-1]))