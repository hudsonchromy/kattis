def polygonArea(X, Y, n):
    
    area = 0

    j = n - 1
    for i in range(0, n):
        area = area + (X[j] + X[i]) * (Y[j] - Y[i])
        j = i

    return(area / 2)

inp = int(input())
while(inp != 0):
    points = inp
    X = []
    Y = []
    for i in range(0, points):
        x, y = map(float, input().split())
        X.append(x)
        Y.append(y)
    area = round(polygonArea(X, Y, points), 1)
    if(area > 0):
        print("CW " + str(area))
    else:
        print("CCW " + str(abs(area)))

    inp = int(input())
