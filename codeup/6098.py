d = [list(map(int, input().split())) for _ in range(10)]

x, y = 1,1

while True:
    if x == 9: break

    if d[x][y] == 0: 
        d[x][y] = 9
        y+=1
    elif d[x][y] == 1: 
        x+=1
        y-=1
    else:
        d[x][y] = 9
        break
        
        
for l in d:
    print(*l)