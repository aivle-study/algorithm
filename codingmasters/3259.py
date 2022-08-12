n=int(input())
a=10**n
b=[]
for i in range(1,a):
    b.append(i)
b=sorted(b,reverse=True)
print(b[1])