def timetosc(time):
    h,m,s=time.split(':')
    h,m,s=int(h),int(m),int(s)
    return h*3600+m*60+s

N,M=input().split()
N,M=int(N),int(M)

pors=[]
for x in range(M):
    st,en=input().split()
    st=timetosc(st)
    en=timetosc(en)
    pors.append([st,en])


count=0
table=[]
for x in range(0,86401):
    for pip in table:
        if pip[1] == x:
            table.remove(pip)
    for pip in pors:
        if pip[0]==x:
            if len(table)<N:
                table.append(pip)
                count+=1


print(count)
    
