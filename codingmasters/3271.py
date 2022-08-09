n = int(input())
p = list(map(int, input().split()))
print(100-sum(p)) if sum(p) < 100 else print(0)