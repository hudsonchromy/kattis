from math import sin, cos, radians, pi

def point_pos(x0, y0, d, theta):
    theta_rad = radians(theta)
    return [x0 + d*cos(theta_rad), y0 + d*sin(theta_rad)]

def average(l, n):
    oneTotal = 0
    twoTotal = 0
    for li in l:
        oneTotal += li[0]
        twoTotal += li[1]
    return ([oneTotal / n, twoTotal / n])

def dist(p1, p2):
    return(((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5)

n = int(input())
while(n != 0):
    positions = []
    for _ in range(n):
        line = input().split()
        at = [float(line[0]), float(line[1])]
        angle = float(line[3])
        for i in range(4, len(line), 2):
            if (line[i] == "walk"):
                at = point_pos(at[0], at[1], float(line[i+1]), angle)
            else:
                angle += float(line[i+1])
        positions.append(at)
    avg = average(positions, n)
    worst = 0
    for pos in positions:
        worst = max(worst, dist(avg, pos))
    print(str(avg[0]) + " " + str(avg[1]) + " " + str(worst))
    n = int(input())
    
