# def color(c1,c2):
#     if c1=='R' and c2=='G':
#         print('Y')
#     elif c1=='G' and c2=='B':
#         print('C')
#     elif c1=='B' and c2=='R':
#         print('M')
#     elif c2=='R' and c1=='G':
#         print('Y')
#     elif c2=='G' and c1=='B':
#         print('C')
#     elif c2=='B' and c1=='R':
#         print('M') 
#     elif c2==c1:
#         print(c1) 
def color(c1,c2):
    if c1=='R' and c2=='G':
        return 'Y'
    elif c1=='G' and c2=='B':
        return 'C'
    elif c1=='B' and c2=='R':
        return 'M'
    elif c2=='R' and c1=='G':
        return 'Y'
    elif c2=='G' and c1=='B':
        return 'C'
    elif c2=='B' and c1=='R':
        return 'M'
    elif c2==c1:
        return c1

n,m=map(int,input().split())
a=[list(input().split()) for _ in range(n)]
b=[list(input().split()) for _ in range(n)]
c=[]

for i in range(n):
   for j in range(m): 
        c.append(color(a[i][j],b[i][j]))
        
if len(c)<=m:
    print(*c)
else: 
    # for i in range(len(c)):
    #     print(c[i],sep="")
    div=m
    end=len(c)
    start=0
    for idx in range(start,end+div,div):
        out=c[start:start+div]
        if out!=[]:
            print(*out)
        start=start+div