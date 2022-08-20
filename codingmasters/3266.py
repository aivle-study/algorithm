n=int(input())
answer=[]
for i in range(n):
    a=input()
    a=int(a)
    if a%2==0:
        answer.append("R")
    else:
        answer.append("L")
for i in range(len(answer)):
    print(answer[i])