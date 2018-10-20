board = []
board.append(list(map(int ,input().split())))
board.append(list(map(int ,input().split())))
board.append(list(map(int ,input().split())))
board.append(list(map(int ,input().split())))
direction =  int(input())
temp = [[],[],[],[]]
def move(inp):
    for k in range(0, 4):
        for _ in range(0, inp[k].count(0)):
            inp[k].remove(0)    
            inp[k].append(0)
        for i in range(0, 3):
            if(inp[k][i] == inp[k][i+1]):
                #print(inp[k][i])
                inp[k][i] = inp[k][i] * 2
                #print(inp[k][i])
                inp[k].pop(i+1)
                inp[k].append(0)
                #print(inp[k][i])

    return(inp)

if(direction == 0): #left
    temp = board
    board = move(temp)
elif(direction == 1): #up
    t = -1
    for i in range(3, -1, -1):
        t+=1
        for j in range(0, 4):
            temp[t].append(board[j][i])
    temp = move(temp)
    board=[[],[],[],[]]
    t = -1
    for i in range(0, 4):
        t+=1
        for j in range(3, -1, -1):
            board[t].append(temp[j][i])
elif(direction == 2): #right
    temp = board
    for k in range(0, 4):
         temp[k].reverse()
    #print(temp)
    temp = move(temp)
    #print(temp)
    for k in range(0, 4): 
        temp[k].reverse()
    board = temp
elif(direction == 3): #down
    t = -1
    for i in range(0, 4):
        t+=1
        for j in range(3, -1, -1):
            temp[t].append(board[j][i])
    temp = move(temp)
    board=[[],[],[],[]]
    t = -1
    for i in range(3, -1, -1):
        t+=1
        for j in range(0, 4):
            board[t].append(temp[j][i])

for i in range(0, 4):
    print("{} {} {} {}".format(board[i][0], board[i][1], board[i][2], board[i][3]))
