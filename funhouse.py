def move(x, y, direction):
    #print(y)
    if(direction == "U"):
        return(up(x, y, False))
    elif(direction == "D"):
        return(down(x, y, False))
    elif(direction == "R"):
        return(right(x, y, False))
    else:
        #print(direction)
        #print(x_)
        return(left(x, y, False))

def up(x, y, found):
    #print("u")
    if(found == False):
        #print(" up @ x {} y {}".format(x,y))
        for i in range(y-1, -1, -1):
            #print(house[i][x])
            if(house[i][x] == "/"):
                #print("x{} y{}".format(x, i))
                coord = right(x, i, False)
                break
            elif(house[i][x] == "\\"):
                #print("here")
                coord = left(x, i, False)
                break
            elif(house[i][x] == "x"):
                coord = (x, i, True)
                break
    else:
        coord = (x, y, True)
    return(coord)
    
def down(x, y, found):
    #print("d")
    if(found == False):
        #print(" down @ x {} y {}".format(x,y))
        for i in range(y+1, L):
            #print(house[i][x])
            #print(" x ={} y ={}".format(x, i))
            if(house[i][x] == "/"):
                coord = left(x, i, False)
                break
            elif(house[i][x] == "\\"):
                coord = right(x, i, False)
                break
            elif(house[i][x] == "x"):
                #print("x {} y {}".format(x, i))
                coord = (x, i, True)
                break
    else:
        coord = (x, y, True)
    #print("q")
    #print(coord)
    return(coord)


def left(x, y, found):
    #print("l")
    #print(" left @ x {} y {}".format(x,y))
    if(found == False):
        for i in range(x-1, -1, -1):
            if(house[y][i] == "/"):
                coord = down(i, y, False)
                break
            elif(house[y][i] == "\\"):
                coord = up(i, y, False)
                break
            elif(house[y][i] == "x"):
                coord = (i, y, True)
                break
    else:
        coord = (x, y, True)
    return(coord)

def right(x, y, found):
    #print("R")
    #print(found)
    #print(" right @ x {} y {}".format(x,y))
    if(found == False):
        for i in range(x+1, W):
            #print(house[y][i])
            #print("{} {}".format(y, i))
            if(house[y][i] == "/"):
                #print("x = {}, y = {}".format(i, y))
                coord = up(i, y, False)
                break
                #print("uu")            
            elif(house[y][i] == "\\"):
                #print("x = {}, y = {}".format(i, x))
                coord = down(i, y, False)
                break
                #print("dd")
            elif(house[y][i] == "x"):
                #print("XX")
                coord = (i, y, True)
                break
    else:
        #pritn("tyt")
        #print("x = {}, y = {}".format(x, y))
        coord = (x, y, True)
    #print("w")
    #print(coord)
    return(coord)

houseCount = 1


while(True):
    W, L = map(int, input().split())
    if(W == 0):
        break
    house = []
    hit = False
    pos = ["x", "y", "d"] # x, y, direction(U, D, R, L)
    for i in range(0, L):
        house.append(list(input()))
    #print(house[1])
    if("*" in house[0]):
        pos[0] = house[0].index("*")
        pos[1] = 0
        pos[2] = "D"
    elif("*" in house[L-1]):
        pos[0] = house[L-1].index("*")
        pos[1] = L - 1
        pos[2] = "U"
    else:
        for i in range(1, L-1):
            if("*" in house[i]):
                pos[1] = i
                pos[0] = house[i].index("*")
                #print(house.index("*"))
                pos[2] = "R" if house[i].index("*") == 0 else "L"
                break
    #print(pos[0], pos[1], pos[2])      
    amper = move(pos[0], pos[1], pos[2])[0: 2]
    house[amper[1]][amper[0]] = "&"
    print("HOUSE " + str(houseCount))
    houseCount += 1
    for i in range(0, len(house)):
        out = ""
        for j in range(0, len(house[0])):
            out += house[i][j]
        print(out)
