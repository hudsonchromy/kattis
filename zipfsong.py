import operator
songNum, outNum = map(int, input().split())
songs = []
for i in range(1, songNum+1):
	listens, name = input().split()
	songs.append([int(listens) * i, songNum - i, name])
songs = sorted(songs, key = operator.itemgetter(0,1), reverse = True)
#print(songs)
for j in range(outNum):
	print(songs[j][2])