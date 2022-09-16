#아이들수, 술래
n,a=map(int,input().split(" "))
m=int(input()) #터치 회수
check=[0]*n #술래 확인 작업
check[a-1]=1 #술래면 1
touch=[input().split(" ") for i in range(m)]
count=1
for i in range(m):
    if check[int(touch[i][0])-1]==1 : #이미 좀비라면
        if check[int(touch[i][1])-1]==0: #당한놈이 아니라면
            count+=1
            check[int(touch[i][1])-1]=1
            
    elif check[int(touch[i][1])-1]==1:
        if check[int(touch[i][0])-1]==0:
            count+=1
            check[int(touch[i][0])-1]=1
        
print(count)
        