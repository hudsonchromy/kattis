inp = input()
while(inp is not None):
    inp = list(map(int, inp.split()))
    print(abs(inp[0] - inp[1]))
    try:
        inp = input()
    except:
        break
