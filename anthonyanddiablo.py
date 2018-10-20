# A = pi (c/2 pi)^2
# c = 2 pi r
import math
A, N = map(float, input().split())
max = math.pi * (N / (2.0 * math.pi))**2
if(max > A):
    print("Diablo is happy!")
else:
    print("Need more materials!")
