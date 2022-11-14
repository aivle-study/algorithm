#https://unpasoadelante.tistory.com/204
from collections import deque

def BFS(graph, root):
    global cnt
    queue = deque([root])
    while queue:
        n = queue.popleft()
        queue += graph[n]
        if n==0:cnt+=1

def spread(graph,start):#최초시작은 0
    print(start,check0[start])
    cnt0=check0[start]
    for x in graph[start]:
        check0[x]+=cnt0
        spread(graph,x)
    # for x in graph[start]:
    #     spread(graph,x)
sumfact=1
sumfect=1
for x in range(50,99):
    sumfact=(sumfact*x)
for x in range(1,50):
    sumfect=(sumfect*x)
resum=sumfact//sumfect
def resu(a,b):
    return a*m+b
def resuback(a):
    return a//m,a%m

def conect(maps,x,y,graph):
    xl=[-1,1,0,0]
    yl=[0,0,-1,1]
    lists=[]
    for i in range(4):
        xx=xl[i]
        yy=yl[i]
        if xx+x<n and yy+y<m and xx+x>=0 and yy+y>=0:
            if maps[xx+x][yy+y]>maps[x][y]:
                lists.append(resu(xx+x,yy+y))
    graph[resu(x,y)]=set(lists)


def DFS(v):
    global cnt
    if v == 0:
        cnt += 1
    if cnt>=10000:
        return 0
    a,b=resuback(v)
    if maps[a][b]>=maps[0][0]:
        return 0
    else:
        for i in graph[v]:
            DFS(i)

n,m=map(int,input().split())

maps=[]
for x in range(n):
    maps.append(list(map(int,input().split())))


graph={}
for x in range(n):
    for y in range(m):
        conect(maps,x,y,graph)
n=n*m

check0=[0]*n
check0[n-1]=1
cnt = 0
counts=0
move=[-m,m,-1,1]
DFS(n-1)

# BFS(graph,n-1)
# spread(graph,n-1)
if cnt==10000:
    print(resum%998244353)
else:
    print(cnt)
# print(check0)