def go(list,start,vis):
    vis[start]=1
    for x in range(n):
        if lists[start][x]=="Y":
            if vis[x]==0:
                go(list,x,vis)

n=int(input())
lists=[]
for x in range(n):
    lists.append(list(input()))

maxscore=0
for x in range(n):
    score=0
    vis=[0]*n
    go(lists,x,vis)
    score=sum(vis)-1
    if maxscore<score:
        maxscore=score
print(maxscore)