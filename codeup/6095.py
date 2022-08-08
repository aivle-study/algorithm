data = []
for i in range(20) : 
  data.append([])
  for j in range(20) :  
    data[i].append(0)

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    data[x][y] = 1
    
for i in range(1, 20) :
  for j in range(1, 20) : 
    print(data[i][j], end=' ') 
  print() 
