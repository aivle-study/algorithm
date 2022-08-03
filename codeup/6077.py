n = int(input())
ans = 0
for i in range(n+1):
    if i % 2 == 0: ans += i
print(ans)