n=int(input())
student=[input().split() for i in range(n)]

student.sort(key=lambda x:x[1],reverse=True)
for i in range(len(student)):
    print(student[i][0],end=' ')