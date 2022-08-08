h,w=map(int,input().split())
n = int(input())

k=[[0 for i in range(w)]for j in range(h)]
#print(d)

for i in range(n):
    l,d,x,y=map(int,input().split())
    
    k[x-1][y-1]=1
    for j in range(l):
        if d==0:
            k[x-1][y-1+j]=1 
        else:
            k[x-1+j][y-1]=1
            
            
for i in range(h):
    for j in range(w):
        print(k[i][j],end=' ')
    print()