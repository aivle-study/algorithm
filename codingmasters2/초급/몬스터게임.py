def dfs(maps,x,y):
    xl=[-1,1,0,0]
    yl=[0,0,-1,1]#상하좌우
    maps[x][y]=0
    for xls,yls in zip(xl,yl):
        if not(x+xls<0 or x+xls>=n or y+yls<0 or y+yls>=m):
            if maps[x+xls][y+yls]==1:
                dfs(maps,x+xls,y+yls)


m,n,K=map(int,input().split())
maps=[[0 for x in range(m)] for x in range(n)]
for x in range(K):
    a,b=map(int,input().split())
    maps[a][b]=1

count=0
for x in range(n):
    for y in range(m):
        if maps[x][y]==1:
            dfs(maps,x,y)
            count+=1
print(count)