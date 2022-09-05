import sys

data = list(map(int,sys.stdin.readline().rstrip()))

sum = data[0]
for i in range(1, len(data)):
    if data[i] <= 1 or sum <= 1:
        sum += data[i]
    else:
        sum *= data[i]
        
print(sum)