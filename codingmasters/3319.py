a,b=input().split(" ")
c=input()
a,b=float(a),float(b)
q="{:."+c+"f}"
print(q.format(a/b))