# 오른쪽 -> 벽 -> 아래
# 0 갈수 있는곳, 1 장애물, 2 먹이
# 맨아래 이거나 못 움직이면, 먹이를 찾으면 끝
#(2,2) 시작
d=[list(map(int,input().split())) for i in range(10)]

x,y=1,1
d[x][y]=9

while True:
    
    if d[x+1][y]==0:
        x+=1
        d[x][y]=9
        continue
    
    if d[x][y+1]==0:
        y+=1
        d[x][y]=9
        continue
    
    if d[x][y+1]==2:
        y+=1
        d[x][y]=9
        break
    
    if d[x+1][y]==2:
        x+=1
        d[x][y]=9
        break 
      
    break        
    
for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()