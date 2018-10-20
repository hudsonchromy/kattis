trans = {}
words = []
while True:
    try:
        eng, foreign = input().split(" ")
        trans[foreign] = eng
    except:
        break
#print(trans)
while True:
    try:
        inp = input()
        if(inp in trans):
            print(trans[inp])
        else:
            print("eh")
    except:
        break
