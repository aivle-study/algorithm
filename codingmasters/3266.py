n = int(input())
num = list(map(int, [input() for _ in range(n)]))
for i in num:
    if i % 2 == 1: print('L')
    else: print('R')