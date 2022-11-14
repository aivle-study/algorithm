def overlab(a,b):
    for x in range(len(a)):
        if a[x]!=0 and b[x]!=0:
            return x
    return -1
def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a
def lcm(a, b): #최소공배수
    return a * b / gcd(a, b)
def mixer(c,d):
    cx=c
    dx=d
    while True:
        ra=min(cx,dx)
        cont=False
        for x in range(2,ra+1):
            if cx%x==0 and dx%x==0:
                cx,dx=cx//x,dx//x
                cont=True
                break
        if cont==True:
            continue
        break
    return cx,dx

n=int(input())
lists=[[0 for x in range(n)]for x in range(n-1)]
for x in range(n-1):
    a,b,c,d=map(int,input().split())
    c,d=mixer(c,d)
    lists[x][a]=c
    lists[x][b]=d
value=lists.pop(0)

while len(lists):
    target=overlab(value,lists[0])
    if target!=-1:
        scrol=lists.pop(0)
        lcvs=lcm(value[target],scrol[target])
        value=list(map(lambda x:x*(lcvs//value[target]),value))
        scrol=list(map(lambda x:x*(lcvs//scrol[target]),scrol))
        scrol[target]=0
        for i in range(n):
            value[i]+=scrol[i]
    else:
        lists.append(lists.pop(0))
for x in value:
    print(int(x),end=" ")

