import decimal
a, b = map(int, input().split())
n= int(input())
decimal.getcontext().prec=n
ans = decimal.Decimal(a)/decimal.Decimal(b)
print(f'{ans:.{n}f}')