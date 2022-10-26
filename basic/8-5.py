#1로 만들기
#연산 4개를 적절히 사용해서 1로 만들기
#사용하는 횟수의 최소
x=int(input())
#보텀업
count=0
d=[0]*30001

# 리스트 값 자체가 횟수 
for i in range(2,x+1):
    d[i]=d[i-1]+1
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    elif i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    elif i%5==0:
        d[i]=min(d[i],d[i//5]+1)
print(d[x])