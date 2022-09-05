import copy
def such1(maps,x,y):
    count=0
    if x+1<5:
        if maps[x+1][y]==1:
            count+=1
    if y+1<5:
        if maps[x][y+1]==1:
            count+=1
    if x+1<5 and y+1<5:
        if maps[x+1][y+1]==1:
            count+=1
    if x-1>=0:
        if maps[x-1][y]==1:
            count+=1
    if y-1>=0:
        if maps[x][y-1]==1:
            count+=1
    if x+1<5 and y-1>=0:
        if maps[x+1][y-1]==1:
            count+=1
    if x-1>=0 and y-1>=0:
        if maps[x-1][y-1]==1:
            count+=1
    if y+1<5 and x-1>=0:
        if maps[x-1][y+1]==1:
            count+=1
    return count

N=int(input())

maps=[]

for x in range(5):
    arr=list(input())
    arr=list(map(int,arr))
    maps.append(arr)

mapstamp=copy.deepcopy(maps)

for le in range(N):
    for x in range(5):
        for y in range(5):
            ct=such1(maps,x,y)
            if ct==2 or ct==3:
                if ct==3:
                    mapstamp[x][y]=1
                else:
                    mapstamp[x][y]=maps[x][y]
            else:
                mapstamp[x][y]=0
    maps=copy.deepcopy(mapstamp)
    mapstamp=copy.deepcopy(maps)

for x in maps:
    for y in x:
        print(y,end="")
    print()
