n = int(input())
answer = 0

for i in range(max(3,n), n*3+1):
    if i % 3 == 0 and i % n == 0: 
        answer = i
        break
        
print(answer)