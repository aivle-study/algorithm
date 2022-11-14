def dfs(grp,start,teff,tusg):
    if len(flag2)!=0:
        return 0
    if teff-tusg>1000:
        flag2.append(1)
        flag.append(1)
        print("INF")
        return 0
    teff+=eff[start]
    if start==end:
        print(teff-tusg)
        flag.append(1)
    for x in range(n):
        ttusg=tusg
        if grp[start][x]!=101:
            ttusg+=grp[start][x]
            dfs(grp,x,teff,ttusg)
n,start,end,m=map(int,input().split())

grp=[[101 for x in range(n)]for y in range(n)]
flag=[]
flag2=[]
for x in range(m):
    a,b,c=map(int,input().split())
    grp[a][b]=c
eff=list(map(int,input().split()))

dfs(grp,start,0,0)
if len(flag)==0:
    print("INCOMPLETE")