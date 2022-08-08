score = list(map(int,input().split()))

avg = sum(score)/len(score)
ans = 'P'

for i in score:
    if i < 40: 
        ans = 'F'
        break 
if avg < 60: ans = 'F'

print(ans)