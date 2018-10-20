inp = int(input())
graph = []
while(inp != 0):
   #print(graph)
   #print("top")
   if(graph != []):
      print("")
   graph = []
   max = 0
   for i in range(0, inp):
      graph.append(list(input()))
      max = len(graph[-1]) if len(graph[-1]) > max else max
   #print("her")
   for i in range(0, len(graph)):
      while(len(graph[i]) != max):
         graph[i].append(" ")
   #print("here")      
   for i in range(0, max):
      outp = ""
      for j in range(len(graph)-1, -1, -1):
         if(graph[j][i] == "|"):
            outp += "-"
         elif(graph[j][i] == "-"):
            outp += "|"
         else:
            outp += graph[j][i]
      while(True):
         if(outp[-1] == " "):
            outp = outp[0: len(outp)-1]
         else:
            break
      print(outp)
   #print(max)
   #print(graph)
   inp = int(input())
