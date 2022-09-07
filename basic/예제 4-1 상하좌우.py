n = int(input())
xy = input().split()

x, y = 1, 1

for i in range(len(xy)):
    if xy[i] == 'U': 
        if x == 1: continue
        else: x -= 1
    if xy[i] == 'D': 
        if x == n: continue
        else: x += 1
    if xy[i] == 'L': 
        if y == 1: continue
        else: y -= 1
    if xy[i] == 'R': 
        if y == n: continue
        else: y += 1
            
print(x, y)