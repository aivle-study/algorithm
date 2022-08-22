n = int(input())
s = [input() for _ in range(n)]

card = list(range(1,n+1))
ans = [0]

for i in range(len(s)):
    if s[i] == 'D':
        ans.insert(0, card[i])
    if s[i] == 'U':
        ans.append(card[i])
        
print(*ans,sep=' ')