inp = []
while True:
	try:
		inp.append(input())
	except EOFError:
		break
dist = 0
if(len(inp[0]) > 9):
	speed = int(inp[0][9:])
else:
	print(inp[0], "0.00", "km")
	speed = 0
time_i = [int(inp[0][0:2]), int(inp[0][3:5]), int(inp[0][6:8])]
for i in range(1, len(inp)):
	time_f = [int(inp[i][0:2]), int(inp[i][3:5]), int(inp[i][6:8])]
	if(len(inp[i]) > 9):
		time = (time_f[0] - time_i[0]) + (time_f[1] - time_i[1]) / 60 + (time_f[2] - time_i[2]) / 3600
		dist += time * speed
		speed = int(inp[i][9:])
	else:
		time = (time_f[0] - time_i[0]) + (time_f[1] - time_i[1]) / 60 + (time_f[2] - time_i[2]) / 3600
		dist += time * speed
		print("%s %.2f %s" % (inp[i], dist, "km"))
	time_i = time_f