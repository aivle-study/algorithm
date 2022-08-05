def evod(a):
    if (a//3==1):
        return "spring"
    if(a//3==2):
        return "summer"
    if(a//3==3):
        return "fall"
    return "winter"


a=input()
a=int(a)
print(evod(a))