import sys

n, m = map(int, sys.stdin.readline().split())

data = []
min_data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
    min_data.append(min(data[i]))
    
print(max(min_data))