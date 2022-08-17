n=list(map(int,input().split(" ")))
avg=sum(n)/len(n)
for i in n:
    if i<40:
        print('F')
        a=0
        break
    else:
        a=1
if a==1 and avg<60:
    print('F')
elif a==1 and avg>=60:
    print('P')
    