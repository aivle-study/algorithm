n = int(input())
p = list(map(int, input().split()))

p = sorted(p, reverse=False) # 오름차순 정렬 
ans = 0 # 그룹 수
total = 0 # 총 그룹원 수

for i in p:
    total += 1
    if total >= i: # 총 그룹원 수 >= 공포도 
        ans += 1
        total = 0
        
print(ans)