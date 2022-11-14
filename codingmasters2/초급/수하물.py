ob,bag=input().split()
ob,bag=int(ob),int(bag)

oblist=[]
baglist=[]
for x in range(ob):
    weight,price=input().split()
    weight,price=int(weight),int(price) 
    oblist.append([price,weight])

for x in range(bag):
    baglist.append(int(input()))

oblist=sorted(oblist,reverse=True)
baglist=sorted(baglist)

bagfull=[0]*len(baglist)
sumprice=0

for obs in oblist:
    for bgs in range(len(baglist)):
        if baglist[bgs]>obs[1]:
            if bagfull[bgs]==0:
                sumprice+=obs[0]
                bagfull[bgs]=1
                break
    if sum(bagfull)==len(baglist):break
print(sumprice)

