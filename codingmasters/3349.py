n = int(input())
x, y = map(int, input().split())
temp = (0**2+n**2)**(1/2)/10 + ((x-0)**2+y**2)**(1/2)/5
ans = 0

if x >= 0:
    for w in range(x+1):
        d1 = (w**2+n**2)**(1/2)
        d2 = ((x-w)**2+y**2)**(1/2)
        t = d1/10 + d2/5
        if t < temp:
            temp = t
            ans = w
else:
    for w in range(0,x+1,-1):
        d1 = (w**2+n**2)**(1/2)
        d2 = ((x-w)**2+y**2)**(1/2)
        t = d1/10 + d2/5
        if t < temp:
            temp = t
            ans = w
print(ans)