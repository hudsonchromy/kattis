turns = [[]]
game = 0
while(True):
    inp = input()
    if(inp == "0"):
        break
    else:
        if(len(turns[game]) % 2 == 1):
            if(inp == "right on"):
                turns[game].append(inp)
                turns.append([])
                game += 1
            else:
                turns[game].append(inp)
        else:
            turns[game].append(int(inp))
#print(turns[0][-2])
for i in range(0, len(turns)-1):
    outp = "Stan may be honest"
    for j in range(1, len(turns[i])-3, 2):
        #print()
        if(turns[i][j] == "too high"):
            #print("h, {}, {}".format(turns[i][-2], turns[i][j-1]))
            if(turns[i][-2] >= turns[i][j-1]):
                outp = ("Stan is dishonest")
                break
        elif(turns[i][j] == "too low"):
            if(turns[i][-2] <= turns[i][j-1]):
                #print("h, {}, {}".format(turns[i][-2], turns[i][j-1]))
                outp = "Stan is dishonest"
                break
    if(turns[i].count(turns[i][-2]) > 1):
        outp = "Stan is dishonest"
    print(outp)
