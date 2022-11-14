from copy import deepcopy
def dfs(maps,x,y):
    if sum(flag1)>0:
        return 0
    maps[x][y]="X"
    if x==targetx and y==(m-1):
        flag1.append(1)
        maps[x][y]="T"
        return 0
    xl=[-1,0,1]
    yl=[1,1,1]#오위,오,오아
    for xls,yls in zip(xl,yl):
        if not(x+xls<0 or x+xls>=n or y+yls<0 or y+yls>=m):
            if maps[x+xls][y+yls]=="O":
                dfs(maps,x+xls,y+yls)
n,m=map(int,input().split())
maps=[]
for x in range(n):
    maps.append(list(input()))

for x in range(n):
    for targetx in range(x+1):
        flag1=[0]
        copymap=deepcopy(maps)
        dfs(maps,x,0)
        if sum(flag1)==0:
            maps=copymap
    for startx in range(x):
        targetx=x
        flag1=[0]
        copymap=deepcopy(maps)
        dfs(maps,startx,0)
        if sum(flag1)==0:
            maps=copymap

cnt=0
for x in maps:
    if x[-1]=='T':
        cnt+=1
print(cnt)