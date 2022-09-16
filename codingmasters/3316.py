#범위가 완전 다를때 어떻게 하셨는지?
# list 30-50온도 
def check(degree,n,min,max,count,c):
    for i in range(c,n):
        if int(degree[i][0])>=min and int(degree[i][0])<=max:
            min=int(degree[i][0]) #15-20
            count+=1
        if int(degree[i][1])>max:
            max=max # 15-20
        if int(degree[i][0])<min :
            min=min #15-30
        if int(degree[i][1])<=max and int(degree[i][1])>min:
            max=int(degree[i][1])
            count+=1
        if int(degree[i][0])>max and int(degree[i][1])>max: #경우가 벗어나는 순간 , 재귀함수
            min=int(degree[i][0])
            max=int(degree[i][1])
            min2,count2=check(degree,min=min,max=max,n=n,count=1,c=i) #재귀함수 => error... 안되는걸까?...
            if count2>count:
                return min2
    return min,count
n=int(input())
degree=[input().split(" ") for i in range(n)]
min=int(degree[0][0]) #15
max=int(degree[0][1] )#30
index=degree[0][0]
min,count=check(degree,min=min,max=max,n=n,count=1,c=1)
print(min)