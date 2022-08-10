n = int(input())
keys = [list(input().split()) for _ in range(n)]
keyword = input()
flag = 0

for i in range(n):
    if keys[i][0] == keyword: 
        print(keys[i][1])
        flag += 1
if flag == 0: print(-1)        