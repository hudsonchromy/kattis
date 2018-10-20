guess = 500
rang= [1, 1001]
#i = 1
print(guess)
while(True):
    inp = input()
    if(inp == "higher"):
        rang[0] = guess
        guess = int(((rang[1] - rang[0])//2) + rang[0])
        #print(rang)
        print(guess)
        #i += 1
    elif(inp == "lower"):
        rang[1] = guess
        guess = int(((rang[1] - rang[0])/2) + rang[0])
        #print(rang)
        print(guess)
        #i += 1
    else:
        break
