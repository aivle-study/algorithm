import sys

a, b, c = map(int,sys.stdin.readline().split())

i = 0

while True:
    i = i + 1

    if i % a == 0 and i % b == 0 and i % c == 0:
        print(i)
        break

