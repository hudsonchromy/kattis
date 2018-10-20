cases = int(input())
DOM = {}
kattis = {}
total = 0
for i in range(0, cases):
    inp = input()
    if(inp not in DOM):
        DOM[inp] = 1
    else:
        DOM[inp] += 1
for i in range(0, cases):
    inp = input()
    if(inp not in kattis):
        kattis[inp] = 1
    else:
        kattis[inp] += 1
for item in DOM:
    if(item in kattis):
        total += min(DOM[item], kattis[item])
print(total)
