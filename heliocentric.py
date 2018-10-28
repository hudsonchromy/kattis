outp = []
case = 1
while True:
	try:
		e, m = map(int, input().split())
		#print(str(e), str(m), "first")
		d = 0

		while(e != 0 or m != 0):
			#print(str(e), str(m))
			e += 1
			m += 1
			d += 1
			e %= 365
			m %= 687
		outp.append("Case ")
		outp.append(str(case))
		outp.append(": ")
		outp.append(str(d))
		outp.append("\n")
		case += 1
	except EOFError:
		print("".join(outp[:-1]))
		break