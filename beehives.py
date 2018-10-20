d = -1
cases = -1
def dist(p1, p2):
    return(((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**.5)
while(d != 0):
    sour = 0
    locations = []
    for i in range(0, cases):
        locations.append(list(map(float, input().split())))
        locations[i].append(0)
    for i in range(0, cases):
        for j in range(i+1, cases):
            if(dist(locations[i], locations[j]) <= d):
                locations[i][2] = 1
                locations[j][2] = 1
            #print("i = {}, j = {}, cases = {}, dist = {}".format(i, j, cases, dist(locations[i], locations[j])))
    #print(locations)
    if(cases > 0):
        for i in range(0, cases):
            if(locations[i][2] == 1):
                sour += 1
        print("{} sour, {} sweet".format(sour, cases-sour))
    d , cases = map(float, input().split())
    cases = int(cases)
