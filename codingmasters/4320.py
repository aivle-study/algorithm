# 깊이우선탐색(DFS)
def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
n,m=map(int,input().split())
graph=[]
visited=[False]*n
for i in range(m):
    graph.append(list(map(int,input().split())))
print(dfs(graph,1,visited))