n = int(input())
r = list(map(int, input().split()))
cnt = [0]*23
for i in r:
    cnt[i-1] += 1
print(*cnt, sep=' ')