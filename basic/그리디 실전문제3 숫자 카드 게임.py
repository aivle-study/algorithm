# 각 행마다의 가장 작은 숫자들 중 가장 큰 수를 고르면 된다.
N, M = map(int, input().split())

min_num = 0

for i in range(N):
    card = list(map(int, input().split()))
    if min(card) > min_num: min_num = min(card)
    # min_num = max(min_num, min(card)) # 해설 참조한 풀이 
        
print(min_num)