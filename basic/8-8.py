# 효율적인 화폐구성
n,m=map(int,input().split())
money=[]
for i in range(n):
    money.append(input())
d=[10001]*(m+1)
d[0]=0
