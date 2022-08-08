n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

data = []
for i in range(24) :
  data.append(0)

for i in range(n) :
  data[a[i]] += 1

for i in range(1, 24) :
  print(data[i], end=' ')
