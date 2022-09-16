def check_area(num):
    m=max(num)
    count={}
    for i in num:
        try:
            count[i]+=1
        except:
            count[i]=1
    if count[m]>=2:
        area=m*m
    else: area=0
    return area
        
n=int(input())
num=list(map(int,input().split()))
#print(num)
a=[]
check=[]
for i in num:
    if i not in a:
        a.append(i)
    else:
        if i not in check:
            check.append(i)
#rint(check) 
if check==[]:
    print(0)
else:
    check=sorted(check,reverse=True)
    #print(check[0],check[1])
    new_area=int((check[0]*check[1]))
    area=check_area(num)
    if check_area(num)==0:
        new_area=int((check[0]*check[1]))
        if new_area>area:
            print(new_area)
    else:
        print(area)