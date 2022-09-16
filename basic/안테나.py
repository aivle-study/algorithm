#안테나(p360)
# 특정 위치의 집에 한개의 안테나 설치
# 모든 거리 총합 최소
# 아이디어 : 1. (지점-각지점) 절대값 최소 구하기? 
#           2. 중앙값? 

n=int(input())
location=list(map(int,input().split()))
location.sort()

def midvalue(lst):
    return [ i for i in sorted(lst)][len(lst) // 2-1]
def midvalue2(lst):
    return [ i for i in sorted(lst)][len(lst) // 2]

a=midvalue(location)
b=midvalue2(location)
sum1=0
sum2=0
for i in range(n):
    sum1+=abs(location[i]-a)
for i in range(n):
    sum2+=abs(location[i]-b)

if sum1<sum2:
    print(a)
elif sum1==sum2:
    print(a)
else:
    print(b)
    