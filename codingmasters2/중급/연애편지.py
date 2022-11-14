from collections import deque
def bfs(grp,start,endlist,visi):
    dist=[2]*n
    que=deque()
    que.append(start)
    visi[start]=True
    while que:
        start = que.popleft()
        for w in grp[start]:
            for x in endlist:
                if x in grp[start]:
                    w=x
            if not visi[w]:
                visi[w]=True
                que.append(w)
                dist[w]=dist[start]+1
                if w in endlist:
                    que.clear()
                    return dist[w]
    return -1
n,k,m=map(int,input().split())
muri=[]
for x in range(m):
    muri.append(set(list(map(int,input().split()))))

startlist=[]
endlist=[]
flag1=0
for x in range(m):
    if 1 in muri[x]:
        startlist.append(x)
    if n in muri[x]:
        endlist.append(x)
    if 1 in muri[x] and n in muri[x]:
        flag1=1

grp=[[]for _ in range(m)]
for x in range(m):
    for y in range(m):
        if len(muri[x] & muri[y])>0 and x!=y:
            grp[x].append(y)
            grp[y].append(x)
        


minresult=10000
for e in startlist:
    result=0
    visi=[False]*n
    result=bfs(grp,e,endlist,visi)
    if minresult>result and result!=-1:
        minresult=result

if flag1==1:
    print(2)
else:
    if minresult!=10000:
        print(minresult)
    else:
        print(-1)

