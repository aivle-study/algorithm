n = int(input())
ai = list(map(int, input().split()))
tg = sum(ai) // n
cnt = 0
while sum(set(ai)) != tg:
    if max(ai) != tg:        
        ai[ai.index(max(ai))] -= 1
    if min(ai) != tg:        
        ai[ai.index(min(ai))] += 1
    cnt += 1        
print(cnt)