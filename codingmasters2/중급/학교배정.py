stu,high=map(int,input().split())

stulist=[]
for x in range(stu):
    stulist.append(list(map(int,input().split())))
stulist=sorted(stulist)
stulist=list(map(lambda x:x[1:],stulist))

visit=[0]*(high+1)
for x in stulist:
    for y in x:
        if visit[y]==0:
            visit[y]=1
            break
print(sum(visit))