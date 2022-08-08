h, w = map(int, input().split())
inp = [[0]*w for _ in range(h)]

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    
    if d == 0:
        for j in range(l):
            inp[x-1][y-1+j] = 1
    else:
        for j in range(l):
            inp[x-1+j][y-1] = 1


for l in inp:
    print(*l)