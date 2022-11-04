#나이 많은 순 
n=int(input())
people=[input().split() for i in range(n)]
people.sort(key=lambda x:x[0],reverse=True)    
for i in range(len(people)):
    print(people[i][1])