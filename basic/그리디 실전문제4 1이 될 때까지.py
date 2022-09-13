N, K = map(int, input().split())
cnt = 0

while N != 1:
    if N%K == 0: # K로 나누어지면 나누고
        N //= K
        cnt += 1
    else: # K로 안나누어지면 1 뺀다
        N -= 1
        cnt += 1
        
print(cnt)