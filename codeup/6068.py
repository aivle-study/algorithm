def evod(a):
    if (a>=90):
        return "A"
    if(a>=70):
        return "B"
    if(a>=40):
        return "C"
    if(a>=0):
        return "D"


a=input()
a=int(a)

print(evod(a))
