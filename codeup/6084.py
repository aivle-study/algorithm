h,b,c,s=input().split(' ')
h,b,c,s=float(h),float(b),float(c),float(s)
print(format((h*b*c*s)/(8*1024*1024),".1f"),"MB")