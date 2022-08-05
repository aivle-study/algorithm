a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
x=1;
while True:
    if x%a==0 and x%b==0 and x%c==0:
        print(x)
        break
    x+=1

