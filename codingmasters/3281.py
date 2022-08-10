n, k = map(int, input().split())
a = list(map(int, input().split()))
m = 0
sl = []

for i in range(n-k+1):
    m = 0
    if 0 in a[i:i+k]: 
        continue
    else: 
        m = sum(a[i:i+k])
    sl.append(m)
print(max(sl))