from math import factorial
def C(a,b):
    return factorial(a)//factorial(b)//factorial(a-b)
n,m=map(int,input().split())
dp=[]
for x in range(1,m+1):
    dp.append((1+(x-1)*(m-x)))
# print(dp)
sums=0
for x in range(n):
    sums+=dp[x]*C(n,x+1)
    sums=sums%1000000007

print(sums)

# 1서버일때 (무조건1포함일때) 1,1,1,1 
# 2서버일때 (무조건12포함일때) 1(2) 2(3) 3(4) 4(5)
# 3서버일때 (무조건123포함일떄) 1(3) 3(4) 5(5) 7(6) 9(7)....  
# 4서버일때 (무조건1234포함일때) 1(4) 4(5) 7(6)....
# 3서버 7클라 = 9
#  = 

# 3서버일떄값 *(5개중 3개선택하는 경우의수)
# 4서버일떄값 *(5개중 4개선택하는 경우의수)=5C4=5!//(4!)//(5-4)!

# 5+(1+(server-1)*(cl-server))


# 1서버일때 (무조건1포함일때) 
# 2서버일때 (무조건12포함일때) 2(1) 
# 3서버일때 (무조건123포함일떄) 3(1) 3C2(2)
# 4서버일때 (무조건1234포함일때) 4C1(1) 4C2(2) 4C3(3)