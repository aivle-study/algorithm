n=int(input())
sum=0
b=0
while sum<n:
    sum+=b
    b+=1
    if sum>=n:
        break
print(sum)