from copy import deepcopy
n,m,k=map(int,input().split())

maxmillist=[]
grp1=[[0 for _ in range(n)]for _ in range(n)]
for x in range(k):
    a,b,c=map(int,input().split())
    a,b=a-1,b-1
    if grp1[a][b]<c:
        grp1[a][b]=c

puregrp1=deepcopy(grp1)
for _ in range(m):
    for x in range(n):
        for y in range(x+1,n):
            if grp1[x][y]!=0:#0이아닌 숫자(즉 갈수있는곳을) 찾으면
                for z in range(y+1,n):
                    if grp1[y][z]!=0:
                        puregrp1[x][z]=max(grp1[x][z],grp1[x][y]+grp1[y][z])
    grp1=puregrp1
    
print(grp1[0][n-1])