import math

def vector(angle, line_length, x1, y1):
    (x2,y2) = (x1 + line_length*math.sin(-angle*math.pi / 180.0), y1 + line_length*math.cos(-angle*math.pi / 180.0))
    return[x2, y2]

cases = int(input())
for i in range(0, cases):
    X = 0
    Y = 0
    angle = 0
    moves = int(input())
    for i in range(0, moves):
        angleIn,  distance = map(float, input().split())
        angle += angleIn
        #print(angle)
        newPoints = vector(angle, distance, X, Y)
        X = newPoints[0]
        Y = newPoints[1]
    print(str(format(X, '.6f')) + " " + str(format(Y, '.6f')))
