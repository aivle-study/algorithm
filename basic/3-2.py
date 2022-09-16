# 큰수의 법칙
# 주어진 수들을 M번 더해서 가장 큰 수 만드는 법칙
# k번 초과해서 더할 수 없음
n,m,k=map(int,input().split()) 
num=list(map(int,input().split()))
num=sorted(num,reverse=True)
a=num[0]
b=num[1]
sum=0
sum=(m//k)*k*a+(m%k)*b
print(sum)