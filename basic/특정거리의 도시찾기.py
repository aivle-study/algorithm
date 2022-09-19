#특정 거리의 도시 찾기(p339)
# N개의 도시 , M개의 도로, 최단거리 K, 출발도시
# 내 아이디어 : DFS -> 연결된 거리를 생각해야하기 때문
# 해설 : 모든 도로의 거리 1 조건 -> 너비우선 탐색
# bfs 원리 : 시작노드 큐 삽입 -> 인접노드 큐에 삽입 방문처리 -> 반복
from collections import deque
n,m,k,x=map(int,input().split())
graph=[[]for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

dis=[-1]*(n+1) #최단거리 초기화
dis[x]=0 #출발도시

#bfs
q=deque([x])  
while q:
    now=q.popleft() #삭제
    for ne in graph[now]: #갈 수 있는 도시 확인
        if dis[ne]==-1: #안갔으면
            dis[ne]=dis[now]+1   #거리 갱신
            q.append(ne) #삽입
check=False
#오름차순뽑기
for i in range(1,n+1):
    if dis[i]==k:
        print(i)
        check=True
if check==False:
    print(-1)

