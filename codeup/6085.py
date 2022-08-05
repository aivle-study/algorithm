r,b,g=input().split()
r,b,g=float(r),float(b),float(g)
print(format((r*b*g)/(8*1024*1024),".2f"),"MB")