import copy
N=int(input())

maps=[[1]]
for le in range(N-1):
    nextmaps=copy.deepcopy(maps)
    nextmaps.insert(0,([0]*(len(maps[0])+1)))
    for i in range(len(nextmaps)):
        for j in range(0,len(nextmaps)-i):
            nextmaps[i][j]=0
            try:nextmaps[i][j]+=maps[i][j]
            except:pass
            try:
                if i-1!=-1:
                    nextmaps[i][j]+=maps[i-1][j]
            except:pass
            try:
                if j-1!=-1:              
                    nextmaps[i][j]+=maps[i][j-1]
            except:pass
        
    maps=copy.deepcopy(nextmaps)

for i in maps:
    for y in i:
        print(y,end=" ")
    print()