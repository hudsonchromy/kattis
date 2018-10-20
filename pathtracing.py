moves = []
graph = [["S"]]
while(True):
    try:
        moves.append(input())
    except EOFError:
        break
#Y X
def listOfSize(n):
    out = []
    for i in range(0, n):
        out.append(" ")
    #print("--{}--".format(out))
    return out
current = [0,0]
size = [1,1]
for move in moves:
    #print(move)


    if(move == "up"):
        if(current[0] - 1 < 0):
            graph.insert(0, listOfSize(size[1]))
            #print("here")
            #print(graph)
            size[0] += 1
            #current[0] -= 1
        else:
            current[0] -= 1
        graph[current[0]][current[1]] = "*" if graph[current[0]][current[1]] != "S" else "S"

        #print(graph)
        #print(graph)
        #graph[current[0]][current[1]] = "*"


    elif(move == "down"):
        if(current[0] + 1 >= size[0]):
            #print("here")
            graph.append(listOfSize(size[1]))
            size[0] += 1
        current[0] += 1
        graph[current[0]][current[1]] = "*" if graph[current[0]][current[1]] != "S" else "S"


    elif(move == "right"):
        if(current[1] + 1 >= size[1]):
            for row in graph:
                row.append(" ")
            size[1] += 1
            current[1] += 1
            graph[current[0]][current[1]] = "*" if graph[current[0]][current[1]] != "S" else "S"
        else:
            current[1] += 1
            graph[current[0]][current[1]] = "*" if graph[current[0]][current[1]] != "S" else "S"



    else:
        if(current[1] -1 < 0):
            for row in graph:
                row.insert(0, " ")
            size[1] += 1
            graph[current[0]][current[1]] = "*" if graph[current[0]][current[1]] != "S" else "S"
        else:
            current[1] -= 1
            graph[current[0]][current[1]] = "*" if graph[current[0]][current[1]] != "S" else "S"
    #print(graph)

graph[current[0]][current[1]] = "E"

#print(graph)
print("#" * (size[1]+2))
for row in graph:
    out = "#"
    for item in row:
        out += item
    print(out + "#")


print("#" * (size[1]+2))
