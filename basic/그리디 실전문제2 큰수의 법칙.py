N, M, K = map(int, input().split()) # M번 더하는데 한번에 K번까지만 더할 수 있음 N = 배열의 크기
num = list(map(int, input().split()))
num = sorted(num, reverse=True)
ans = 0

ans = num[1]*(M//K) + num[0]*(M-(M//K))
print(ans)