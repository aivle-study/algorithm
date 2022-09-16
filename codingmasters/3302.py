n,m=map(int,input().split(" "))
sum=[0]*n #금액

m=[input().split(" ") for i in range(2*m)]
price=[]
for i in range(0,len(m),2):
    x=int(int(m[i][0])/int(m[i][1]))
    price.append(x)

pr=0
for i in range(1,len(m),2):
    for j in range(len(m[i])):
        p=int(m[i][j])-1 #
        if j==(len(m[i])-1): #해당 끝 부분이라면
            pr+=1
        if pr>=len(price): #price길이보다 길면
            pr-=1
        print(pr,p)
        sum[p]=sum[p]+price[pr]
print(sum)
