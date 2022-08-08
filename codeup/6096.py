data = []
for i in range(20) : 
  data.append([])
  for j in range(20) :  
    data[i].append(0)

for i in range(19):
    a = input().split()
    for j in range(19):
        data[i+1][j+1] = int(a[j])


n = int(input())

for i in range(n) :
  x, y = map(int, input().split())
  for j in range(20) :
    if data[j][y]==0 :
      data[j][y]=1
    else :
      data[j][y]=0

    if data[x][j]==0 :
      data[x][j]=1
    else :
      data[x][j]=0
      
for i in range(1, 20) :
  for j in range(1, 20) : 
    print(data[i][j], end=' ') 
  print() 