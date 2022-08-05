a,m,d,n=input().split(" ")
a,m,d,n=int(a),int(m),int(d),int(n)
prev=a
for i in range(n):
    prev=m*d+1
print(prev)