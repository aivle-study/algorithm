N, M = map(int, input().split())

bill = [0]*N

for _ in range(M):
    C, n = map(int, input().split())
    i = list(map(int, input().split()))
    for j in i:
        bill[j-1] += int(C/n)
    
print(*bill)