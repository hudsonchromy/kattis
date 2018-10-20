cases = int(input())
for i in range(0, cases):
    inp = list(map(int, input().split()))
    total = 0
    for i in range(1, inp[0]+1):
        total += inp[i]
    avg = total / inp[0]
    total = 0
    for i in range(1, inp[0]+1):
        if(inp[i] > avg):
            total += 1
    above = total / inp[0]
    #print("my a = {}".format(total))   
    print(str("{:.3f}".format(above*100)) + "%" )
