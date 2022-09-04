N = int(input())

if N > 60:
    s = N%60
    m = N//60
else: 
    s = N
    m = 0
    
H, M, S = 11, 59, 60

print(f'{H:0>2}:{M-m:0>2}:{S-s:0>2}')