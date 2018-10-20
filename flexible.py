width, numPartitions = map(int, input().split())
paritions = list(map(int, input().split()))
posibilities = set({})
paritions.append(0)
paritions.append(width)
#print(paritions)
for i in range(0, numPartitions+2):
    for j in range(0, numPartitions+2):
        #print(abs(paritions[i] - paritions[j]))
        posibilities.add(abs(paritions[i] - paritions[j]))
posibilities.remove(0)
posibilities = list(posibilities)
outp = ""
for item in sorted(posibilities):
    outp += str(item) + " "
print(outp)
