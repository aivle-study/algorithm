data = []

for i in range(10):
    data.append(list(map(int, input().split())))

x, y = 1, 1

while True:
    if data[x][y] == 0:
        data[x][y] = 9
    elif data[x][y] == 2:
        data[x][y] = 9
        break
    
    if (data[x][y+1] == 1 and data[x+1][y] == 1):
        break
    if data[x][y+1] != 1:
        y += 1
    elif data[x+1][y] != 1:
        x += 1

for i in range(10):
    for j in range(10):
        print(data[i][j], end = ' ')
    
    print()
    