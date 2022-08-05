def evod(a):
    if (a % 2 == 0):
        if(a>0):
            return 'C'
        else:
            return 'A'
    else:
        if (a > 0):
            return 'D'
        else:
            return 'B'

a=input()
a=int(a)

print(evod(a))