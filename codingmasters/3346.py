from itertools import permutations

n=input()
num=list(map(str,str(n)))
a=list(permutations(num,len(num)))
b=0
for i in range(len(a)):
    new="".join(a[i])
    b=new
    if int(new) %13==0:#조합 합치기
        print("YES")
        b=new
        break
    
if int(b) %13!=0 :
    print('NO')
    