stops = int(input())
stopList = list(map(int, input().split(" ")))
diction = {}
stopList.sort()
#print(stopList)
i = 0
while(True):
    #print("stopList")
    if(i >= len(stopList)-2):
        break
    #print("{} {}".format(stopList[i], stopList[i+2]))
    if(stopList[i] == (stopList[i+2] - 2)):
        j = 2
        while(True):
            #print("{} {}".format(stopList[i], stopList[i+j] - j))
            #print(diction)
            #print(stopList)
            if((i + j) >= len(stopList)):
                break
            if(stopList[i] == stopList[i + j] - j):
                j += 1
            else:
                break
        diction[stopList[i]] = stopList[i + j-1]
        for k in range(i, j):
            #print("p")
            stopList.pop(i)
    else:
        #print("--------------------")
        diction[stopList[i]] = None
        stopList.pop(i)
for item in stopList:
    diction[item] = None
out = ""
for key in diction:
    if(diction[key] != None):
        out += ("{}-{} ".format(key ,diction[key]))
    else:
        out += "{} ".format(key)
print(out)
