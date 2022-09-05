
hour,minute,second=input().split(":")
hour,minute,second=int(hour),int(minute),int(second)
t=int(input())
n=int(input())-1
N=t*n

second=second+N%60
while True:
    if second>=60:
        minute+=1
        second-=60
    else:break

m=(N%3600)//60
minute=minute+m
while True:
    if minute>=60:
        hour+=1
        minute-=60
    else:break

h=N//3600
hour=hour+h
while True:
    if hour>=24:
        hour-=24
    else:break

print(format(hour, '02')+':'+format(minute, '02')+':'+format(second, '02'))