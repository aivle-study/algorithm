a,b,c=map(int,input().split(' '))
m=max(a,b,c)
if a==m:
    print(int(b*c/2))
elif b==m:
    print(int(a*c/2))
else:
    print(int(b*a/2))