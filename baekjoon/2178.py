# https://www.acmicpc.net/problem/2178
# 미로 탐색
# 1: 이동할 수 있는 칸, 0: 이동할 수 없는 칸
# 최소 칸수 구하기
# 시도 알고리즘 : bfs(가까운 노드 부터 차례대로 지나가기)
from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
    
# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))