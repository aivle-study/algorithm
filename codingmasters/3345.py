s=[input() for _ in range(5)]
check=[]
for i in range(5):
    for j in range(5):
        if s[i][j]=='#':
            check.append([i,j])
print(check)
print(set(check[0]).difference(set(check[3])))
count=0
for i in range(len(check)):
    for j in range(len(check[0])):
        if len(set(check[0]).difference(set(check[3])))==2: #차집합
            a=0
            count+=1
            print("NO")
            break
        else: a=1
        break
    break
if a!=0 and count==0:
    print("YES")