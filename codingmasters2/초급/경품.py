def go(resh,start,los):
    vis[start]=1
    if los+1<=2:
        for x in range(N):
            if resh[start][x]==1:
                go(resh,x,los+1)


N,M=map(int,input().split())
resh=[[0 for x in range(N)]for x in range(N)]
for x in range(M):
    a,b=input().split()
    a,b=int(a)-1,int(b)-1
    resh[a][b]=1
    resh[b][a]=1
vis=[0]*N
go(resh,0,0)
print(sum(vis)-1)

