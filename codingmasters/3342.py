arr1=input()
arr2=input()

yes=0
for x in range(len(arr2)):
    if arr1==arr2:yes=1
    arr2=arr2[-1]+arr2[:-1]
    
print("YES" if yes==1 else "NO")