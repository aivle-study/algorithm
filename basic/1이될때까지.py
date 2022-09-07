N,K=input().split()
N,K=int(N),int(K)
sum=0
b=N
while True:
    if b==1:
        break
    a=b%K
    sum+=a
    b=(b-a)//K
    sum+=1
print(sum)