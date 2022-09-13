n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

d[x][y] = 1 # 입력 좌표 = 방문한 것으로 처리 

dx = [-1, 0, 1, 0]    # 북, 동, 남, 서
dy = [0, 1, 0, -1]    # 북, 동, 남, 서

turn_cnt = 0
cnt = 1

def turn():
    global direction
    direction -= 1
    if direction == -1: direction = 3

while True:
    turn()
    nx, ny = x+dx[direction], y+dy[direction] # 방향 바라보기 
    
    if d[nx][ny] == 0 and arr[nx][ny] == 0: # 바라본 방향이 육지면
        d[nx][ny] = 1
        x, y = nx, ny
        turn_cnt = 0
        cnt += 1
        continue
    else: # 바라본 방향이 바다거나 가본 곳이면 
        turn_cnt += 1 # 돌아
        
    if turn_cnt == 4: # 네번 다 돌았는데
        nx, ny = x-dx[direction], y-dy[direction]
        if arr[nx][ny] == 0: # 뒤로 갈 수 있으면 뒷걸음질
            x, y = nx, ny
        else: # 뒤도 바다면 걍 끝 
            break
        turn_cnt = 0
        
print(cnt)