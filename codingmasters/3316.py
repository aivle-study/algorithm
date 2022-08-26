# #범위가 완전 다를때 어떻게 하셨는지?
# n=int(input())
# degree=[input().split(" ") for i in range(n)]
# min=int(degree[0][0]) #15
# max=int(degree[0][1] )#30
# count=0
# index=degree[0][0]
# for i in range(1,n):
#     if int(degree[i][0])>=min and int(degree[i][0])<=max:
#         min=int(degree[i][0]) #15-20
#         count+=1
#     if int(degree[i][1])>max:
#         max=max # 15-20
#     if int(degree[i][0])<min :
#         min=min #15-30
#     if int(degree[i][1])<=max and int(degree[i][1])>min:
#         max=int(degree[i][1])
#         count+=1
# print(min,count)
#범위가 완전 다를때 어떻게 하셨는지?

def check(degree,n,min,max):
    count=1
    min2=0
    count2=0
    for i in range(1,n):
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
        if int(degree[i][0])>max:
            count=1
            min2,count2=check(degree=degree,min=min,max=max,n=n)
            if count2>count:
                return min2
    return min,count
n=int(input())
degree=[input().split(" ") for i in range(n)]
min=int(degree[0][0]) #15
max=int(degree[0][1] )#30
index=degree[0][0]
min,count=check(degree=degree,min=min,max=max,n=n)
print(min)
#print(min,count)