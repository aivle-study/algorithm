n=int(input())
num=list(map(int,input().split()))
#print(num)
num_check=[]
for i in range(len(num)-2):
    num_check.append(num[i:i+3])
#print(num_check)
max=sorted(num_check[0])[1]
for i in range(1,len(num_check)):
    a=sorted(num_check[i])
    #print(a)
    if max<a[1]:
        max=a[1]
print(max)