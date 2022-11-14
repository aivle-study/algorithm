import sys
sys.setrecursionlimit(2000)
def dfs(grap, v, visited):
    visited[v]=True    #시작노드 방문처리
    print(v,end=" ")
    for i in sorted(grap[v]):         #시작노드와 인접한노드 순차적 탐색
        if not visited[i]:
            dfs(grap, i, visited)



lens,n=input().split()
lens,n=int(lens),int(n)
road=[]
grap=[[]for x in range(lens+1)]
visited=[0]*(lens+1)

for i in range(n):
    S,D = map(int, input().split())
    grap[S].append(D)
    grap[D].append(S)

dfs(grap, 1, visited)