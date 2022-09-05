time=input()
h,m,s=time.split(":")
t=int(input())
n=int(input())
if n==1:
    print(time)
else:
    h,m,s=int(h),int(m),int(s) 
    x=t*(n-1)+s # 31*2+30 =92
    if x>=60:
        # print(x)
        # print(x//60,x%60)
        m+=(x//60)
        s=x%60
        if m>=60:
            h+=(m//60)
            m=(m%60)
        if h>=24:
            h=0
    h=str(h).zfill(2)
    m=str(m).zfill(2)
    s=str(s).zfill(2)
    print(h+':'+m+":"+s)
        
