import sys
sys.setrecursionlimit(10000000)
def dfs(maps,x,y):
    xl=[-1,1,0,0]
    yl=[0,0,-1,1]#상하좌우
    if maps[x][y]=="A":
        cntA.append(1)
    elif maps[x][y]=="B":
        cntB.append(1)
    maps[x][y]="X"
    for xls,yls in zip(xl,yl):
        if not(x+xls<0 or x+xls>=n or y+yls<0 or y+yls>=m):
            if maps[x+xls][y+yls]!="X":
                dfs(maps,x+xls,y+yls)


n,m=input().split()
n,m=int(n),int(m)
maps=[]
for x in range(n):
    maps.append(list(input()))

sumA=0
sumB=0
for x in range(n):
    for y in range(m):
        if maps[x][y]=='A' or maps[x][y]=='B':
            cntA=[]
            cntB=[]
            dfs(maps,x,y)
            if sum(cntB)>=sum(cntA):
                sumB+=sum(cntB)
            else:
                sumA+=sum(cntA)

print(sumA,sumB)