a=input()
d=list(map(int,a.split()))
c=[1000,1500,2000,3000,5000]
sum=0
for x,y in zip(d,c):
    sum+=x*y
print(sum)