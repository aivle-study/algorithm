n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

from collections import deque

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    
    queue = deque()
    queue.append((x,y))
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 네 방향으로의 위치 확인 
        for i in range(4): # 4방향
            nx, ny = x+dx[i], y+dy[i]
            
            # 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            
            # 벽인 경우 (0) 무시
            if arr[nx][ny] == 0: continue
            
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y]+1 # 직전 노드 값 + 1
                queue.append((nx, ny)) # 반복을 위해 큐에 추가
                
    return arr[n-1][m-1] # 마지막 칸의 값


print(bfs(0,0))