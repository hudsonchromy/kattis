import math



def polarAngle(pointMain, point2):
	if(startPoint == point2):
		return(3)
	if((pointMain[1] == point2[1])):
		return(2)
	return math.atan((point2[0]-pointMain[0])/(point2[1]-pointMain[1]))

def area(A, B, C):
	x=0
	y=1
	return (A[x]*(B[y]-C[y]) + B[x]*(C[y]-A[y]) + C[x]*(A[y]-B[y]))/2



pointNum = int(input())


while(pointNum != 0):
	points = []
	stack = list(range(pointNum))
	for i in range(0, pointNum):
		points.append(list(map(int, input().split())))
	minY = points[0][1]
	minX = points[0][0]
	for point in points:
		if(point[1] < minY):
			minY = point[1]
			minX = point[0]
		elif(point[1] == minY and point[0] < minX):
			minX = point[0]
	startPoint = [minX, minY]
	for point in points:
		point.append(polarAngle(startPoint, point))

	# print(stack)
	points.sort(key=lambda x: x[2], reverse = True)

	for i in range(0, pointNum-1):
		if(points[i][2] == points[i+1][2]):
			if(math.hypot(points[i][0], points[i][1]) > math.hypot(points[i+1][0], points[i+1][1])):
				stack.pop(i+1)
			else:
				stack.pop(i)

	# print(stack)
	# print("----------")

	i = 0
	while(i <= len(stack)+1):
		# print(points[stack[(i+1) % len(stack)]])
		are = area(points[stack[i % len(stack)]], points[stack[(i+1) % len(stack)]], points[stack[(i+2) % len(stack)]])
		# print(are)
		if(are < 0):
			stack.pop((i+1) % len(stack))
		i += 1
		
	# print("-----------")
	# print(stack)
	# #print(are)
	# print(points)
	# print(minX)
	# print(minY)

	# print("------------")
	print(len(stack))
	for num in stack:
		print("{} {}".format(points[num][0], points[num][1]))

	pointNum = int(input())

