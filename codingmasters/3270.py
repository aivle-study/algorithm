a, b = map(int, input().split())
x, y = map(int, input().split())

if a <= x:
    if (x-a)+y >= b: print('YES')
    else: print('NO')
else: print('NO')