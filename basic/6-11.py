# 성적이 낮은 순서로 학생 출력하기
n=int(input())
student=[]
for i in range(n):
    in_d=input().split()
    student.append((in_d[0],int(in_d[1])))
student=(sorted(student))
for i in range(n):
    print(student[i][0],end=' ')