# 이른, 성적 입력시 성적이 낮은 순서대로 학생의 이름 출력
from operator import itemgetter


n=int(input())
student=[input().split() for i in range(n)]
dic={}
for i in range(n):
    dic[student[i][0]]=student[i][1]
dic=dict(sorted(dic.items(),key=lambda x:x[1]))
for key in dic.keys():
    print(key,end=' ')