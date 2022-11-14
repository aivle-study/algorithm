from copy import deepcopy
def spread(maps,num):
    resultmaps=deepcopy(maps)
    xl=[-1,1,0,0]
    yl=[0,0,-1,1]
    for x in range(n):
        for y in range(m):
            if maps[x][y]==num:
                for xx,yy in zip(xl,yl):
                    if x+xx>=0 and x+xx<n and y+yy>=0 and y+yy<m:
                        if maps[x+xx][y+yy]<num:
                            resultmaps[x+xx][y+yy]=num
    return resultmaps
n,m=map(int,input().split())
maps=[]
for x in range(n):
    maps.append(list(map(int,input().split())))
result=0
while True:
    result+=1
    ct=0
    good=0
    for x in range(n):
        for y in range(m):
            if maps[x][y]==1:
                ct+=1
                if x==0 or y==0 or x==n-1 or y==m-1:
                    good=1
                    break
    if ct==0:
        print("IMPOSSIBLE")
        break
    if good==1:
        break
    maps=spread(maps,1)
    maps=spread(maps,2)

if good==1:
    print(result)