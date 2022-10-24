# 데이트 자본주의

# 최대한 비싼 상대부터 만나기
# 돈의 범위 안에서 
#최대 가능한 수 출력

money,people=map(int,input().split())
p_money=list(map(int,input().split()))
p_money.sort(reverse=True)
#print(p_money[-1])
count=0
while money>=p_money[-1]:
    if count==people:
        break
    for i in range(len(p_money)):
        if p_money[i]<=money:
            count+=1
            money-=p_money[i]
            #print(money)
print(count)