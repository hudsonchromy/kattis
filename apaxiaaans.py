inp = list(input())
i = 0
while(i< len(inp)-1):
    if(inp[i] == inp[i+1]):
        inp.pop(i+1)
    else:
        i += 1
out = ""
for char in inp:
    out += char
print(out)
