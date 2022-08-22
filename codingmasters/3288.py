from collections import Counter

n = int(input())
stick = list(map(int, input().split()))

cnt = dict(Counter(stick))
rec = {}
area = 0

for i in list(set(stick)):
    if cnt[i] >= 2: 
        rec[i] = cnt[i]
        
rec = sorted(rec.items(), reverse=True)

if len(rec) == 1 and rec[0][1] < 4: 
    area = 0
elif len(rec) == 0: 
    area = 0
else:
    if rec[0][1] >= 4:
        area = rec[0][0]**2
    else:
        area = rec[0][0] * rec[1][0]
    
print(area)