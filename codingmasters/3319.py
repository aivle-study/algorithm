from decimal import Decimal, getcontext

a,b=input().split(" ")
c=int(input())
a,b=float(a),float(b)
getcontext().prec=c #자리수 설정 -> 안떨어지는 소수점?....
x=Decimal(a)/Decimal(b)
x=str(x)
print(x.ljust(c+2,"0"))
# 91534765137.0 1000000000000.0 50\r\n0.091534765137\r\n