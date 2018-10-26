#tutorial.py
import math
calcs, n, comp = map(int, input().split())

def factorial(n, g):
	fact = 1
	for i in range(1,n+1):
		if(fact <= g):
			fact = fact * i
		else:
			return fact
	return(fact)

complexity = [0, lambda x: factorial(x, calcs), lambda x:2**x, lambda x: x**4, lambda x: x**3, lambda x: x**2, lambda x: x * math.log(x,2), lambda x: x]

if(complexity[comp](n) > calcs):
	print("TLE")
else:
	print("AC")