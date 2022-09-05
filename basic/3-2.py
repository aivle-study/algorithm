import sys

n, m, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

data.sort(reverse = True)

first = data[0]
second = data[1]

result = (k * (m//(k+1)) + m % (k+1)) * first + (m//(k+1)) * second

print(result) 