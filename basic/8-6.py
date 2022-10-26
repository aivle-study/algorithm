# 개미전사
#keypoint : 어디를 더할것인가?
n=int(input())
stock=list(map(int,input().split()))
# 1번과 2번을 중점적으로 봐야할듯
# 1번 아니면 2번 띄어진 stock 더하자
d=[0]*100
d[0]=stock[0]
d[1]=max(stock[0],stock[1])
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+stock[i])
print(d[n-1])