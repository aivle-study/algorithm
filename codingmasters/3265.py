a,b=map(int,input().split(" "))
if b>a:
    min=b-a
    if min> a+(60-b):
        min=a+(60-b)
else:
    min=a-b
    if min> b+(60-a):
        min=b+(60-a)
print(min)