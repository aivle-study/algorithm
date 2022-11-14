def dfs(grp,start,visi):#dfs
    visi[start]=1
    for x in range(len(grp[start])):
        if grp[start][x]==1:
            if visi[x]==0:
                dfs(grp,x,visi)
                
n,m=map(int,input().split())

grp=[[0 for x in range(n)]for y in range(n)]
visi=[0]*n
for x in range(m):
    a,b=input().split()
    a,b=int(a)-1,int(b)-1
    grp[a][b]=1
    grp[b][a]=1

count=0
for x in range(n):
    if visi[x]==0:
        dfs(grp,x,visi)
        count+=1

print(count)
        