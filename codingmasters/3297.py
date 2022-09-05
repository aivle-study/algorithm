a,b,abl=input().split()
x,y,xyl=input().split()
a,b,abl,x,y,xyl=int(a),int(b),int(abl),int(x),int(y),int(xyl)
if (abs(a-x)<=(abl/2 + xyl/2)) and (abs(b-y)<=(abl/2 + xyl/2)):
    print("YES")
else:
    print("NO")

