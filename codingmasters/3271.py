n=input()
tem=0
for i in range(len(n)):
    a=map(int,input().split(" "))
tem=sum(a)
if tem>=100:
    print(0)
else:
    #print(sum(a))
    tem=100-tem
    print(tem)