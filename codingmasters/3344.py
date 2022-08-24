A = input()
B = input()

ans = 'YES'
temp = A
for j in range(len(B)):
    if temp.find(B[j]) == -1:
        ans = 'NO'
        break
    temp = temp[temp.find(B[j]):]
    
print(ans)    