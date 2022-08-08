from math import pi

a, b, c = map(int, input().split())
A = pi*(a**2)
B = pi*(b**2)*c

print('NO') if B < A else print('YES')