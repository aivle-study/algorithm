# 플로이드(p385)
# n개의 도시, m개의 버스 
# (A,B) 최소 비용
n=int(input())
m=int(input())

#무한
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

#자기자신
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

#bus info            
for _ in range(m):
    a,b,c=map(int,input().split())
    #graph[a][b]=c
    #가장 짧은 간선 정보만 저장
    if c<graph[a][b]:
        graph[a][b]=c

#플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print('0',end=' ')
        else:
            print(graph[a][b],end=' ')
    print()