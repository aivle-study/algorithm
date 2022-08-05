def evod(a):
    if (a % 2 == 0):
        return 'even'
    else: 
        return 'odd'
    
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

print(evod(a))
print(evod(b))
print(evod(c))