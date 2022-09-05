a,b,D,d=list(input().split())
a,b,D,d=int(a),int(b),int(D),int(d)

sumsD=4
sumsd=4
if a%D==0:
    sumsD+=((a//D)-1)*2
else:
    sumsD+=(a//D)*2

if b%D==0:
    sumsD+=((b//D)-1)*2
else:
    sumsD+=(b//D)*2

sumsd+=((a//d-1)+(b//d-1))*2

if sumsD>sumsd:
    print(-1)
else:
    print(sumsD,sumsd)