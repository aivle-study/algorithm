s=input() #문자열
x=s
n=int(input())
change=[input().split(" ") for i in range(n)]
#print(change)
for i in range(n):
    if change[i][0] in x:
        s=s.replace(change[i][0],change[i][1])
        print(s)
    elif change[i][0] not in x:
        print(s)
    
