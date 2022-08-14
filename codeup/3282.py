n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    sum=0
    for j in range(m):
        sum=0
        sum+=s[i][j]
        
        if i-1<0: sum+=0
        else: sum+=s[i-1][j]
        if j-1<0: sum+=0
        else: sum+=s[i][j-1]
        
        if i+1==n: sum+=0
        else: sum+=s[i+1][j]
        if j+1==m: sum+=0
        else: sum+=s[i][j+1]

        if sum > ans: ans = sum
            
print(ans)