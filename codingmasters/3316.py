N = int(input())
temp = [list(map(int, input().split())) for _ in range(N)]
temp2 = [0]*32

for i in range(N):
    l = list(range(temp[i][0], temp[i][1]+1))
    for j in l:
        temp2[j] += 1
        
print(temp2.index(max(temp2)))