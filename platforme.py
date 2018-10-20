from operator import itemgetter

def finder(newx1, newx2, newy, built):
    #print(built)
    #print(newx1 + 0.5)
    #print(built[0][2])
    for i in range(len(built)-1, -1, -1):
        #print("i")
        #print(i)
        #print(built[i][1])
        if(newx1 + 0.5 > built[i][1] and newx1 + 0.5 < built[i][2]):
            needed = newy - built[i][0]
            break
    for i in range(len(built)-1, -1, -1):
        if(newx2 - 0.5 > built[i][1] and newx2 - 0.5 < built[i][2]):
            needed += newy - built[i][0]
            return(needed)





platformNum = int(input())
platforms = []
pBuilt = [[0, 0, 10001]]
total = 0
for i in range(0, platformNum):
    platforms.append(list(map(int, input().split())))
platforms = sorted(platforms, key = itemgetter(0))
#print(platforms)
for i in range(0, platformNum):
    total += finder(platforms[i][1], platforms[i][2], platforms[i][0], pBuilt)
    pBuilt.append(platforms[i])
    #print(pBuilt)
print(total)
