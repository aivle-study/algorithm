#우박수열
n=int(input())
print(int(n),end=" ")
while n>1:
    if n%2==0:
        n=n/2
        
    else:
        n=3*n+1
    print(int(n),end=" ")  