N=list(input())
alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

col=[]
row=''
for x in N:
    if x in alp:
        col.append(x)
    else:
        row+=x

orgc="".join(col.copy())
orgr=str(row)
col=list(map(ord,col))

col[-1]=col[-1]-1
while col.count(64):
    for x in range(len(col)):
        if col[x]==64:
            if x==0:
                del col[x]
                break
            else:
                col[x]+=26
                col[x-1]-=1

col="".join(list(map(chr,col)))
row=str(int(row)-1)

print(col+orgr)
print(orgc+row)
