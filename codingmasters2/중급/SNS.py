def dfs(grp,stt,visi):
    visi[stt]=1
    for x in range(n):
        if grp[stt][x]==1:
            if visi[x]==0:
                dfs(grp,x,visi)

n,m=map(int,input().split())
grp=[[0 for y in range(n)]for x in range(n)]
for x in range(m):
    a,b=input().split()
    a,b=int(a)-1,int(b)-1
    grp[b][a]=1


maxnum=0
maxlist=[]
for x in range(0,n):
    visi=[0]*(n)
    dfs(grp,x,visi)
    if maxnum==sum(visi):
        maxlist.append(x)
    if maxnum<sum(visi):
        maxlist=[]
        maxnum=sum(visi)
        maxlist.append(x)


for x in maxlist:
    print(x+1,end=" ")
