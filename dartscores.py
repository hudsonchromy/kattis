def points(dist):
    if(dist <= 20):
        score = 10
    elif(dist <= 40):
        score = 9
    elif(dist <= 60):
        score = 8
    elif(dist <= 80):
        score = 7
    elif(dist <= 100):
        score = 6
    elif(dist <= 120):
        score = 5
    elif(dist <= 140):
        score = 4
    elif(dist <= 160):
        score = 3
    elif(dist <= 180):
        score = 2
    elif(dist <= 200):
        score = 1
    else:
        score = 0
    return(score)

cases = int(input())
for _ in range(0, cases):
    throws = int(input())
    scoreT = 0
    for _ in range(0, throws):
        x, y = map(int, input().split())
        dist = (x**2 + y**2)** 0.5
        scoreT += points(dist)
    print(scoreT)
