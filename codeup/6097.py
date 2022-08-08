h, w = map(int, input().split())
n = int(input())

data = [[0]*w for i in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())
    
    for j in range(l):
        if d == 0:
            data[x-1][y-1+j] = 1
        else:
            data[x-1+j][y-1] = 1

for i in range(h):
    for j in range(w):
        print(data[i][j], end = ' ')
    print()
    
