#앨라배마 해변 쥐
import math
n,m=(input().split(' '))
n,m=int(n),int(m)
map=[input() for i in range(n)]
check=[[1]*m for i in range(n)]
a,b=(input().split(' '))
x_i,y_i='0','0'
x_i2,y_i2='0','0'
for i in range(n):
    for j in range(m):
        #땅 vs 바다 
        if map[i][j]!='g':
            check[i][j]=0 #살수 있음
        if map[i][j]=='o': #바다
            x_i=i
            y_i=j
        if map[i][j]=='c': #들고양이
            x_i2=i
            y_i2=j
for i in range(n):
    for j in range(m):
        if abs(i-x_i)+abs(j-y_i)<=int(a):
           check[i][j]=0
        if abs(i-x_i2)+abs(j-y_i2)<=int(b):
           check[i][j]=0        
print(check)
