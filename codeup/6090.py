a,m,d,n=input().split(" ")
a,m,d,n=int(a),int(m),int(d),int(n)
for i in range(n-1):
    a = a*m+d
print(a)