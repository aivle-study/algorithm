from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny<0 or nx>=n or ny>=m:
                continue
            if maps[nx][ny]==0:
                continue
            
            if maps[nx][ny] ==1:
                maps[nx][ny] = maps[x][y]+1
                queue.append((nx,ny))

    return maps[n-1][m-1]

n,m=input().split()
n,m=int(n),int(m)

maps=[]
for x in range(n):
    arr=list(map(int,input()))
    maps.append(arr)

print(bfs(0,0))

