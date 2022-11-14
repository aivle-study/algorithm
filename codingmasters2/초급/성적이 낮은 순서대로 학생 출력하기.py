n=int(input())
student=[]
for x in range(n):
    name,score=input().split()
    score=int(score)
    student.append([score,name])
for x in sorted(student,reverse=True):
    print(x[1],end=" ")