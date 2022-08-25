N, A = map(int, input().split())
M = int(input())
nums = [list(map(int, input().split())) for _ in range(M)]

cnt = 1
it = {A}

for i in range(M):
    if len(it.intersection(nums[i])) == 1:
        cnt += 1
        it.update(nums[i])
        
print(cnt)