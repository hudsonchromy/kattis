trans = {'a': '2', 'b': '22', 'c':'222', 'd':'3', 'e':'33', 'f':'333', 'g':'4', 'h':'44', 'i':'444', 'j':'5', 'k':'55', 'l':'555', 'm':'6', 'n':'66', 'o':'666', 'p':'7', 'q':'77', 'r':'777', 's':'7777', 't':'8', 'u':'88', 'v':'888', 'w':'9', 'x':'99', 'y':'999', 'z':'9999', ' ':'0'}
cases = int(input())
for j in range(cases):
    inp = list(input())
    outp = trans[inp[0]]
    for i in range(1, len(inp)):
        #print(outp[-1])
        if(trans[inp[i]][0] == outp[-1]):
            outp += " " + trans[inp[i]]
        else:
            outp += trans[inp[i]]
    print("Case #{}: ".format(j+1) + outp)
