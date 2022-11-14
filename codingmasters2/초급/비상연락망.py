a=int(input())
b=list(map(int,input().split()))
bud=[]
for x in range(1,a+1):
    bud.append([x,b[x-1]])
attack=[1]
count=0
while len(bud):
    ct=0
    attacks=[]
    while ct!=len(bud):
        if bud[ct][1] in attack:
            attacks.append(bud.pop(ct)[0])
            if len(bud)==0:break
        else:
            ct+=1
    attack=attacks

    count+=1
    # print(bud,attack)
if a==1:
    print(0)
else:
    print(count)