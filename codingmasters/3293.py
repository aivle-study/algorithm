from itertools import combinations
n=input()
a=list(input().split())
a=list(map(int,a))
sort_a=sorted(a)
check=list(range(0,len(a)))
x=list(combinations(check,2))
len2=[]
c=1
for i in range(len(x)):
    y=a[x[i][0]:x[i][1]]
    new_y1=a[:x[i][0]]
    new_y2=a[x[i][1]:]
    y=sorted(y)
    z=new_y1+y+new_y2
    print(z)
    if sort_a==z:
        len2.append(x[i][1]-x[i][0])
        c=0
        break
    break
if c==0:
    print(min(len2))
elif c==1:
    print(len(a)-1)       
# 135 298 467 141 665 750 843 802   