n = int(input())
sum = 0
i = 0
while True:
    sum += i
    i += 1
    
    if(sum >= n):
        break
print(sum)