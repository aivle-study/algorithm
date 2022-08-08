import sys
a, m, d, n = map(int,sys.stdin.readline().split())
num = 0

for i in range(1,n):
    a = (m * a) + d
print(a)
