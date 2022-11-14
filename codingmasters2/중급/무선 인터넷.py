n=int(input())
maps=[]
for x in range(n):
    maps.append(list(map(int,input().split())))
gong=[]
house=[]
for x in range(n):
    for y in range(n):
        if maps[x][y]==1:house.append([x,y])
        if maps[x][y]==2:gong.append([x,y])

minsum=10000
for go in gong:
    sums=0
    for hs in house:
        sums+=abs(go[0]-hs[0])+abs(go[1]-hs[1])
    if minsum>sums:minsum=sums

print(minsum)