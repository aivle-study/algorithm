N,M,K=input().split()
N,M,K=int(N),int(M),int(K)
arr=input().split()
arr=sorted(map(int,arr))
sum=(M//(K+1))*(arr[-1]*K+arr[-2])
sum+=(M%(K+1))*arr[-1]
print(sum)
