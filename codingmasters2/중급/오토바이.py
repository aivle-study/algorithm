def dfs(grp,start):
    if start==((n*n)-1):
        cnt.append(1)
        return 0
    if start in grp.keys():
        for x in grp[start]:
            dfs(grp,x)
    # for x in range(n*n):
    #     if grp[start][x]==1:
    #         dfs(grp,x)
    
def nums(x,y):
    return x*n+y

n=int(input())
maps=[]
for x in range(n):
    maps.append(list(map(int,input().split())))

# grp=[[0 for x in range(n*n)]for y in range(n*n)]
grp={}
for x in range(n):
    for y in range(n):
        lists=[]
        if maps[x][y]!=0:
            gasol=maps[x][y]
            if gasol<(n-y):
                # grp[nums(x,y)][nums(x,y+gasol)]=1
                lists.append(nums(x,y+gasol))
            if gasol<(n-x):
                # grp[nums(x,y)][nums(x+gasol,y)]=1
                lists.append(nums(x+gasol,y))
            grp[nums(x,y)]=set(lists)

cnt=[]
dfs(grp,0)
print(sum(cnt))