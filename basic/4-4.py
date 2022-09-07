# 게임개발
# N*M 크기 직사각형, 육지 or 바다
# (A,B) 북쪽으로 떨어진 칸 개수, 서쪽
# 바다 갈 수 없음
# 왼쪽 방향부터 차례대로 갈곳 정함
# 안간곳 있다면 회전 후 전진, 없다면 회전만
# 모두 가거나 바다인경우 방향 유지후 한칸 뒤로 가기
# 뒤로 못가는 경우 stop
n,m=map(int,input().split()) # n*m
x,y,d=map(int,input().split())
#방문처리 
check=[[0]*m for _ in range(n)]
check[x][y]=1 # 1이면 방문처리
stat=[input().split() for _ in range(n)]
#방향
dx=[-1,0,1,0] #북동남서
dy=[0,1,0,-1] #북동남서
count=1 # 현재 칸 포함
time=0
#일단 바다 및 현재 상황 1 처리
for i in range(n):
    for j in range(m):
        if stat[i][j]=='1':
            check[i][j]=1
print(check)
while True:
    d-=1
    if d==-1:
        d=3
    nx=x+dx[d]
    ny=x+dy[d]
    if check[x][y]==0 and stat[nx][ny]==0:
        check[nx][ny]=1
        x,y=nx,ny
        count+=1
        time+=1
    else: #못가는 상황
        time+=1
    if time==4:
        nx=x-dx[d]
        ny=y-dy[d]
        if stat[nx][ny]==0:
            x,y=nx,ny
        else:
            break
        time+=1
print(count)
        
    
        
    


