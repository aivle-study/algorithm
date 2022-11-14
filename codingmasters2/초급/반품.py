from math import prod


n,price=input().split()
n,price=int(n),int(price)

prodlist=[]
for x in range(n):
    prodlist.append(int(input()))
prodlist=sorted(prodlist,reverse=True)

count=0
for x in prodlist:
    if price>=x:
        price-=x
        count+=1
print(count)