cases = int(input())
operations = ["+","-","*","//"]
def find(num):
    outf = "no solution"
    for j in range(0, 4):
        for h in range(0, 4):
            for g in range(0, 4):
                if(eval("4{}4{}4{}4".format(operations[j], operations[h], operations[g])) == num):
                    outf = ("4 {} 4 {} 4 {} 4 = {}".format(operations[j], operations[h], operations[g], num))
                    outf = outf.replace("//", "/")
    return(outf)
for i in range(0, cases):
    out = ""
    inp = int(input())
    out += find(inp) 
    if(inp < -60 or inp > 256 or out == "no solution"):
        print("no solution")
    else:
        #print("here")
        print(out)
