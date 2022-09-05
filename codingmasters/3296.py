def times(first):
    sum=0
    h,m,s=first.split(":")
    sum+=int(h)*3600+int(m)*60+int(s)
    return sum

meter=int(input())
N=int(input())

cars={}
for x in range(N):
    carnum,timess=input().split()
    cars[carnum]=times(timess)

for x in range(N):
    carnum,timess=input().split()
    start=cars[carnum]
    last=times(timess)
    if start>last:
        timess+=86400
    hour=(last-start)/3600
    cars[carnum]=int(meter/hour)

for x in sorted(cars.keys()):
    print(x,cars[x])
