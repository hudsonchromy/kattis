time = (int(input()) - 2018) * 12
out = "no"
for i in range(time, time+12):
    if(i % 26 == 3):
        out = "yes"
print(out)
