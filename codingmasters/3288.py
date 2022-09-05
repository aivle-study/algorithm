dumi=input()
arr=input().split()
arr=list(map(int,arr))
a=[]
new_arr = [] 
for x in arr:
    if x not in a: 
        a.append(x)
    else:
        if x not in new_arr:
            new_arr.append(x)
new_arr=sorted(new_arr)
print(new_arr[-1]*new_arr[-2])
