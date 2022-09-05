arr1=input()
arr2=input()

count=0
for x in arr1:
    if arr2[count]==x:
        if count==len(arr2)-1:
            count+=1
            break
        else:
            count+=1

if count==len(arr2):
    print("YES")
else:
    print("NO")