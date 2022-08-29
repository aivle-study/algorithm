N = int(input())
temp = 0

for i in range(2, N):
    if N%i == 0: temp += 1
if N == 1: temp = 1
        
print('clap') if temp == 0 else print(N)