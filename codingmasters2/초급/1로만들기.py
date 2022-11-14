x=int(input())
count=0
while x!=1:
    count+=1
    if x%5==0:
        x=x//5
        continue
    if x%3==0:
        x=x//3
        continue
    if (x-1)%5==0:
        x-=1
        continue
    if x%2==0:
        x=x//2
        continue

    x-=1
print(count)