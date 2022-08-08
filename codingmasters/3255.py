n, m = map(int, input().split())
a = [list(input().split()) for _ in range(n)]
b = [list(input().split()) for _ in range(n)]
c = [[0]*m for _ in range(n)]
temp = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        temp[i][j] = a[i][j] + b[i][j]

for k in range(n):
    for l in range(m):
        if temp[k][l][0] == temp[k][l][1]:
            c[k][l] = temp[k][l][0]
        elif temp[k][l] == 'RG' or temp[k][l] == 'GR':
            c[k][l] = 'Y'
        elif temp[k][l] == 'GB' or temp[k][l] == 'BG':
            c[k][l] = 'C'
        else: c[k][l] = 'M'
            
for x in c: print(*x)