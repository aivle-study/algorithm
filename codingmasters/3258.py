n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
x, y = 0, 0

for i in range(n):
    if a[i][0] == a[i][1]:
        continue
    if a[i][0] == 1:
        if a[i][1] == 2: y+=1
        else: x+=1
    elif a[i][0] == 2:
        if a[i][1] == 1: x+=1
        else: y+=1
    else:
        if a[i][1] == 1: y+=1
        else: x+=1
            
print(x,y)