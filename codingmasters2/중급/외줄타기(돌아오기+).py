INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n,m =map(int,input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[[INF,x] for x in range(n+1)] for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b][0] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b][0] = c
    graph[b][a][0] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b][0] = min(graph[a][b][0], graph[a][k][0] + graph[k][b][0])

#다시 자기자신에게의 거리 무한으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b][0] = INF


def dfs(grap, v, visited):
    visited[v]=1    #시작노드 방문처리
    for i in sorted(grap[v])[:-2]:         #시작노드와 인접한노드 순차적 탐색
        if visited[i[1]]==0:
            sums.append(i[0])
            dfs(grap, i[1], visited)
            break



minsum=INF

for x in range(1,n):
    sums=[]
    visited=[0]*(n+1)
    dfs(graph,x,visited)
    if minsum>sum(sums):
        minsum=sum(sums)

print(minsum)