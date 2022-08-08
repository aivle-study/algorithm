ba = [list(map(int, input().split())) for _ in range(1,20)]

n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    
    for j in range(19):
        if ba[x-1][j]==0: ba[x-1][j]=1
        else: ba[x-1][j]=0
            
        if ba[j][y-1]==0: ba[j][y-1]=1
        else: ba[j][y-1]=0

for l in ba:
    print(*l)