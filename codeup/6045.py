a=input()
b=[]
b=a.split(" ")
b=list(map(int,b))
print(sum(b),format(sum(b)/len(b),".2f"))