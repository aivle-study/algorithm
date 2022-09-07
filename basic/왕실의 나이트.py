xy=input()
x=ord(xy[0])-96
y=int(xy[1])

count=8
if x in[7,2]:count-=2
if y in[7,2]:count-=2
if x in[8,1]:count-=3
if y in[8,1]:count-=3
print(count)
