from collections import deque
def bfs(maps,xylist):
    visi=[]
    queue=deque(xylist)
    xl=[-1,1,0,0]
    yl=[0,0,-1,1]
    while queue:
        a=queue.popleft()
        for xls,yls in zip(xl,yl):
            if not(a[0]+xls<0 or a[0]+xls>=n or a[1]+yls<0 or a[1]+yls>=m):
                if  maps[a[0]+xls][a[1]+yls]==0:
                    maps[a[0]+xls][a[1]+yls]=maps[a[0]][a[1]]+1
                    queue+=[[a[0]+xls,a[1]+yls]]

n,m=map(int,input().split())
maps=[]
for x in range(n):
    maps.append(list(map(int,input().split())))

xylist=[]
for x in range(n):
    for y in range(m):
        if maps[x][y]==1:
            xylist.append([x,y])

bfs(maps,xylist)
flag1=0
maxnums=0
for x in range(n):
    for y in range(m):
        if maps[x][y]==0:
            flag1=1
        if maxnums<maps[x][y]:
            maxnums=maps[x][y]
if flag1==0:
    print(maxnums-1)
else:
    print(-1)
# for x in maps:
#     print(x)
