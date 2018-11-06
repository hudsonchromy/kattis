import math

cases = int(input())
for _ in range(cases):
	directions = int(input())
	theta = 0
	points = []
	for _ in range(directions):
		move = list(input().split())
		
		if(move[0] == "fd"):
			#print("theta ", theta)
			dist = int(move[1])
			#print(dist * math.sin(theta))
			points.append([(dist * math.sin(math.radians(theta))), (dist * math.cos(math.radians(theta)))])
		elif(move[0] == "bk"):
			dist = -1 * int(move[1])
			points.append([(dist * math.sin(math.radians(theta))), (dist * math.cos(math.radians(theta)))])
		elif(move[0] == "lt"):
			theta += int(move[1])
			#print("theta ", theta)
		else:
			theta -= int(move[1])
			#print("theta ", theta)
	xsum = 0
	ysum = 0
	for point in points:
		xsum += point[1]
		ysum += point[0]
	print(int(round(math.sqrt(xsum**2 + ysum**2))))
#print(100 * math.sin(math.radians(120)))
#print(100 * math.sin(math.radians(240)))