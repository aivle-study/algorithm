a,d,n=input().split(" ")
a,d,n=int(a),int(d),int(n)
prev=a
for i in range(n-1):
    prev*=d
print(prev)