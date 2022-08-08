# 오른쪽 -> 벽 -> 아래
# 0 갈수 있는곳, 1 장애물, 2 먹이
# 맨아래 이거나 못 움직이면, 먹이를 찾으면 끝
#(2,2) 시작
d=[list(map(int,input().split())) for i in range(10)]

x,y=1,1

while True:
    if d[x][y]==0:
        d[x][y]=9
    elif d[x][y]==2:
        d[x][y]=9
        #먹이를 찾은 경우
        break
    
    #갈곳이 없는 경우
    if (d[x][y+1]==1)and(d[x+1][y]==1):
        break
    
    if d[x][y+1]!=1:
        y=y+1
    if d[x+1][y]!=1:
        x=x+1
        
    
for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()