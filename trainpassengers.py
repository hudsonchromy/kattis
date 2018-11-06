capacity, stations = map(int, input().split())
peeps = 0
outp = "possible"
for station in range(1, stations + 1):
	left, entered, stayed = map(int, input().split())
	peeps += (entered - left)
	#print("peeps", peeps)
	if(capacity < peeps or capacity < 0): #purple
		#print(1000)
		outp = "impossible"
		break
	if(peeps != capacity and stayed != 0): #blue
		#print(2000)
		outp = "impossible"
		break
	if(station == 1 and left != 0):
		outp = "impossible"
		break
	if(station == stations and peeps != 0): #green
		#print(3000)
		#print("peeps", peeps)
		outp = "impossible"
		break
	if(station == stations and stayed != 0): #red
		#print(4000)
		outp = "impossible"
		break
print(outp)