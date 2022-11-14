
N=int(input())
M=int(input())
maps=[[10000 for x in range(N+1)]for x in range(N+1)]

for x in range(M):
    a,b=map(int,input().split())
    maps[a][b]=1
    maps[b][a]=1
for x in range(1,N+1):
    maps[x][x]=0

for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            maps[a][b]=min(maps[a][b],maps[a][k]+maps[k][b])

minmax=10000
x=0
for x in range(1,len(maps)):
    if minmax>max(maps[x][1:]):
        minmax=max(maps[x][1:])
        good=x
print(good)

