n, m = map(int, input().split())
k = 100 * m / n
print('YES') if k <= 4 else print('NO')