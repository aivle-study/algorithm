#위에서 아래로
n=int(input())
num=[]
for i in range(n):
    num.append(int(input()))
num=sorted(num,reverse=True)
for i in range(n):
    print(num[i],end=' ')
