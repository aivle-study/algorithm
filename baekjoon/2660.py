# https://www.acmicpc.net/problem/2660
# 회장뽑기
# 가까운 정도에 따라 점수 부여
# 모든 회원과 친구 :1
# 다른 모든 회원이 친구 or 친구의 친구 :2
# 다름 모든 회원이 친구 or 친구의 친구 or 친구의 친구의 친구 : 3
# 회장은 가장 점수가 작은 사람
INF=int(1e9)
n=int(input())#회원수
member=[[0]*(n+1) for _ in range(n+1)]
while True:
    m1,m2=map(int,input().split())
    #while문 탈출
    if m1==m2==-1:
        break
    member[m1][m2]=1
    member[m2][m1]=1
    
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            member[a][b]=min(member[a][b],member[a][k]+member[k][b])

score=[]
for i in range(1,n+1):
    score.append(max(member[i][1:]))
answer=min(score)
cand=score.count(answer)
print(answer,cand)


    
    