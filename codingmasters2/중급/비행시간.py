N=int(input())
M=int(input())
INF = int(1e9)
maps=[[INF for x in range(N+1)]for x in range(N+1)]

for x in range(M):
    a,b,c=map(int,input().split())
    maps[a][b]=min(c,maps[a][b])


for k in range(1,N+1):
    maps[k][k]=0
    for a in range(1,N+1):
        for b in range(1,N+1):
            maps[a][b]=min(maps[a][b],maps[a][k]+maps[k][b])

for x in range(N+1):
    for y in range(N+1):
        if maps[x][y]==INF:maps[x][y]=0

for x in maps[1:]:
    for y in x[1:]:
        print(y,end=" ")
    print()

