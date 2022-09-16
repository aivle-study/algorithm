# 모험가 n명 
# 공포도 x인 모험가는 반드시 x명 이상의 모험가 그룹 참여
# 최대 몇명 모험가? -> 최소 공포 사용
n=int(input())
scare=list(map(int,input().split()))
count=0
group=0 #모험가 수 
scare=sorted(scare)
for i in scare:
    group+=1
    if group >= i :
        count+=1
        group=0
print(count)
    