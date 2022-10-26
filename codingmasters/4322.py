# 이른, 성적 입력시 성적이 낮은 순서대로 학생의 이름 출력
from operator import itemgetter


n=int(input())
student=[input().split() for i in range(n)]

student.sort(key=lambda x:x[1])
for i in range(len(student)):
    print(student[i][0],end=' ')