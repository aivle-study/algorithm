n=int(input())
work=[]
for x in range(n):
    a,b=input().split()
    a,b=int(a),int(b)
    work.append([x,a,b])#인덱스,걸리는시간,상여금


lits=[[]for _ in range(n+1)]
lits[0].append(0)
for x,a,b in work:
    w=max(lits[x])+b
    if x+a<=n:
        lits[x+a].append(w)
    if x<n:
        lits[x+1].append(max(lits[x]))
    # print(lits)
print(max(lits[-1]))

