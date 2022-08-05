a=input()
a=int(a,16)

for x in range(1,16):
    print('%X'%a,'*%X'%x,'=%X'%(a*x),sep="")