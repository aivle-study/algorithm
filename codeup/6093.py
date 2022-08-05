n = int(input())
r = list(map(int, input().split()))

for i in range(len(r)-1,-1,-1):
    print(r[i], end=' ')