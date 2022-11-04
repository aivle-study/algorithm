#학생들의 등수
n=int(input())
student=list(map(int,input().split()))
studnet2=student.copy()
studnet2.sort(reverse=True)
for i in range(n):
    print(student[i],studnet2.index(student[i])+1)