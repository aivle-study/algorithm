a,b=input().split(" ")
a,b=int(a),int(b)
a_list=[]
b_list=[]
for i in range(1,a):
    if a%i==0:
        a_list.append(i)
for i in range(1,b):
    if b%i==0:
        b_list.append(i)
        
if sum(a_list)==b and sum(b_list)==a:
    print("YES")
else:
    print("NO")