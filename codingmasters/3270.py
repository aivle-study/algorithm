# if b>y -> (b-y)+a 
# if b<y ->
a,b=map(int,input().split(' '))
x,y=map(int,input().split(' '))
if b>=y:
    if x>=(b-y)+a:
        print("YES")
    else:
        print("NO")
elif b<y:
    if x>=(y-b)+a:
        print("YES")
    else:
        print("NO")
        