# 두배열의 원소 교체
# 최대 k번 바꿈
# 배열 A의 모든 원소 합 최대 
# 아이디어 : A의 최소랑 B의 최대 바꾸기
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=sorted(a)
b=sorted(b,reverse=True)
for i in range(k):
    tem=a[i]
    a[i]=b[i]
    b[i]=tem
print(sum(a))
    