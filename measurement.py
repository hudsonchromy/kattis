inp = input()
num, start, whatever, end = inp.split()
num = int(num)
units = [1000, 12, 3, 22, 10, 8, 3]
position = {"thou":0, "th":0, "in":1, "inch":1, "foot":2, "ft":2, "yard":3, "yd":3, "chain":4, "ch":4, "furlong":5, "fur":5, "mile":6, "mi":6, "league":7, "lea":7}
pos_from = position[start] #inch = 1
pos_to = position[end] # ft = 2
if(pos_from > pos_to):
    #print("=={} {}==".format(pos_to, pos_from))
    for i in range(pos_from-1, pos_to-1, -1):
        #print("u= {}".format(units[i]))
        num *= units[i]
else:
    for i in range(pos_from, pos_to):
        num /= units[i]
print(num)
