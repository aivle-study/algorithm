#떡볶이 떡 만들기(p201)
#아이디어 : max-1 ~ 1까지 거꾸로 계산
n,m=map(int,input().split()) # 떡의 개수, 떡의 길이
leng=list(map(int,input().split()))
big=max(leng)-1
sum=0
answer=[]
for j in range(big,0,-1):
    sum=0
    for i in range(n):
        if j>leng[i]:
            #print(abs(leng[i]))
            sum+=0
        else:
            #print(j,"*",abs(leng[i]-j))
            sum+=abs(leng[i]-j)
            #print("sum",sum)
            if sum>=m:
                answer.append(j)
print(max(set(answer)))             
                
        
        
