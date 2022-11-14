from copy import deepcopy
from collections import deque
import sys
sys.setrecursionlimit(10000)
def dfswood(maps,x,y):
    xl=[-1,1,0,0]
    yl=[0,0,-1,1]#상하좌우
    maps[x][y]=2
    for xls,yls in zip(xl,yl):
        if not(x+xls<0 or x+xls>=n or y+yls<0 or y+yls>=m):
            if maps[x+xls][y+yls]==0:
                dfswood(maps,x+xls,y+yls)

def bfs(maps,x,y):
    visi=[]
    queue=deque([[x,y]])
    xl=[-1,1,0,0]
    yl=[0,0,-1,1]
    maps[x][y]=1
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
    maps.append(list(map(int,list(input()))))

dfswood(maps,0,0)

xl=[-1,1,0,0]
yl=[0,0,-1,1]
mapscopy=deepcopy(maps)
for x in range(n):
    for y in range(m):
        if maps[x][y]==2:
            for xls,yls in zip(xl,yl):
                if not(x+xls<0 or x+xls>=n or y+yls<0 or y+yls>=m):
                    mapscopy[x+xls][y+yls]=2
maps=mapscopy
for x in range(n):
    for y in range(m):
        if maps[x][y]==2:
            maps[x][y]=0

bfs(maps,0,0)

if maps[n-1][m-1]==0:
    print(-1)
else:
    print(maps[n-1][m-1])
