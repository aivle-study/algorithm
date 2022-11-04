# 데이트 자본주의

# 최대한 비싼 상대부터 만나기
# 돈의 범위 안에서 
#최대 가능한 수 출력

# 1000 8
# 874 98 48 32 5 5 3 2
money,people=map(int,input().split())
p_money=list(map(int,input().split()))
p_money.sort(reverse=True)
count=0
sum=0
while True:
    if count==people:
        break
    for i in range(len(p_money)):
        if sum<=money:
            sum+=p_money[i]
            count+=1
        else:
            sum+=0
            count+=0
    break    
print(count)   