def dfs(maps,x,y):
    xl=[-1,1,0,0]
    yl=[0,0,-1,1]#상하좌우
    maps[x][y]=1
    for xls,yls in zip(xl,yl):
        if not(x+xls<0 or x+xls>=n or y+yls<0 or y+yls>=m):
            if maps[x+xls][y+yls]==0:
                dfs(maps,x+xls,y+yls)


n,m=input().split()
n,m=int(n),int(m)
maps=[]
for x in range(n):
    maps.append(list(map(int,input())))

count=0
for x in range(n):
    for y in range(m):
        if maps[x][y]==0:
            dfs(maps,x,y)
            count+=1
print(count)