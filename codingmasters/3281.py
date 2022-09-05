N,K=input().split()
N,K=int(N),int(K)
arr=list(map(int,input().split()))

maxsum=0
for x in range(N-K+1):
    sums=0
    impos=0
    for y in range(K):
        if arr[x+y]==0:
            impos=1
            break
        sums+=arr[x+y]
    if sums>maxsum and impos==0:
        maxsum=sums
print(maxsum)