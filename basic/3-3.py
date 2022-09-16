#숫자 카드 게임
# 가장 높은 숫자가 쓰인 카드 한장 뽑는 게임
# N*M 형태 행열
n,m=map(int,input().split())
num=[input().split() for i in range(n)]
num=sorted(num)
min=num[0][0]
for i in range(n):
    if min>num[i][0]:
        min=num[i][0]
print(min)
        