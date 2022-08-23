from itertools import *
n=int(input())
a=n//1000
b=(n-a*1000)//100
c=(n-a*1000-b*100)//10
d=(n-a*1000-b*100-c*10)
x=list(permutations([a,b,c,d],2))
# print(x[0][0])
# print(sum(x[0]))
# li=[a,b,c,d]
# li.remove(x[0][0])
# li.remove(x[0][1])
# print(sum(li))
for i in range(len(x)):
    sum(x[i])
    li=[a,b,c,d]
    li.remove(x[i][0])
    li.remove(x[i][1])
    if sum(x[i])==sum(li):
        print("YES")
        q=0
        break
    else: q=1
if q==1:
    print("NO")