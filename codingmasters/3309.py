hour=12
minute=0
second=0
N=int(input())



second=second-N%60
while True:
    if second<0:
        minute-=1
        second+=60
    else:break

m=N//60
minute=minute-m
while True:
    if minute<0:
        hour-=1
        minute+=60
    else:break

h=N//3600
hour=hour-h
while True:
    if hour<0:
        hour+=24
    else:break

print(format(hour, '02')+':'+format(minute, '02')+':'+format(second, '02'))