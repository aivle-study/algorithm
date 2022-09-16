n=int(input())
h=12 #시각
m=0 # 분
s=0 # 초
while n>=1 and n<=1000:
    if n>60: # 오바되면
        h-=1
        m=60-(n//60)-1
        s=60-(n%60)
        if m>=60:
            h=60-(m//60)
            m=12-(m%60)
    else: #오바아니면
        s=60-n
        m=60-1
        h-=1
    h=str(h).zfill(2)
    m=str(m).zfill(2)
    s=str(s).zfill(2)
    print(h+":"+m+":"+s)
    break