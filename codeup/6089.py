a, r, n = map(int,input().split())
cnt = 1
while cnt < n:
    a *= r
    cnt += 1
print(a)