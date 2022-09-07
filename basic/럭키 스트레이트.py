a=list(map(int,list(input())))
left=a[:len(a)//2]
right=a[len(a)//2:]
if sum(left)==sum(right):
    print('LUCKY')
else:
    print('READY')
