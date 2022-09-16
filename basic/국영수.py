#국영수(p359)
# 국어 감소 -> 영어 증가 -> 수학 감소 -> 이름 사전순
n=int(input())
student=[]
for _ in range(n):
    #student.append(input().split())
    data=input().split()
    student.append([data[0],int(data[1]),int(data[2]),int(data[3])])
#print(student)
student=sorted(student, key=lambda x:(-x[1],x[2],-x[3],x[0]))
#student.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in range(n):
    print(student[i][0])