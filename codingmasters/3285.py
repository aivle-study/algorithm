n=int(input())
home=list(map(int,input().split()))
location=[input().split() for i in range(n)]
#print(home,location)
min=abs(home[0]-int(location[0][0]))+abs(home[1]-int(location[0][1]))
for i in range(1,n):
    if min>abs(home[0]-int(location[i][0]))+abs(home[1]-int(location[i][1])):
        min=abs(home[0]-int(location[i][0]))+abs(home[1]-int(location[i][1])) 
print(min*100)