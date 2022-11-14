def U(cube,zero):
    # if 3 in [cube[0][1][0],cube[0][0][0],cube[0][1][1],cube[0][0][1]]:
    #     weight["U"]+=1
    if zero==True:
        cube[0][1][0],cube[0][0][0],cube[0][1][1],cube[0][0][1]=cube[0][0][0],cube[0][0][1],cube[0][1][0],cube[0][1][1]
        return cube    
    else:
        cube[0][0][0],cube[0][0][1],cube[0][1][0],cube[0][1][1]=cube[0][1][0],cube[0][0][0],cube[0][1][1],cube[0][0][1]
        return cube
def L(cube,zero):
    if 3 in [cube[1][0][0],cube[0][0][0],cube[1][1][0],cube[0][1][0]]:
        if zero:
            weight["L"]-=1
        else:
            weight["L"]+=1
    if zero==True:
        cube[1][0][0],cube[0][0][0],cube[1][1][0],cube[0][1][0]=cube[0][0][0],cube[0][1][0],cube[1][0][0],cube[1][1][0]
        return cube  
    else:
        cube[0][0][0],cube[0][1][0],cube[1][0][0],cube[1][1][0]=cube[1][0][0],cube[0][0][0],cube[1][1][0],cube[0][1][0]
        return cube
def F(cube,zero):
    if 3 in [cube[1][1][0],cube[0][1][0],cube[1][1][1],cube[0][1][1]]:
        if zero:
            weight["F"]-=1
        else:
            weight["F"]+=1
    if zero==True:
        cube[1][1][0],cube[0][1][0],cube[1][1][1],cube[0][1][1]=cube[0][1][0],cube[0][1][1],cube[1][1][0],cube[1][1][1]
        return cube  
    else:
        cube[0][1][0],cube[0][1][1],cube[1][1][0],cube[1][1][1]=cube[1][1][0],cube[0][1][0],cube[1][1][1],cube[0][1][1]
        return cube
cube=[[[1,2],
        [3,4]],
        [[5,6],
        [7,8]]]
cubecopy=[[[1,2],
        [3,4]],
        [[5,6],
        [7,8]]]
weight={"F":0,"L":0}
n=int(input())
pattern=[]
for x in range(n):
    arr=input()
    a,b=0,0
    if len(arr)>1:
        a=arr[0]
        b=True
    else:
        a=arr
        b=False
    pattern.append([a,b])

cnt=0
while True:
    for al,rev in pattern:
        if al=="U":
            cube=U(cube,rev)
        if al=="F":
            cube=F(cube,rev)
        if al=="L":
            cube=L(cube,rev)
    cnt+=1
    if cube==cubecopy:
        if weight["L"]==0 and weight["F"]%2==0:
            if weight["F"]%4==0:
                break
        else:
            if weight["F"]%3==0:
                break
print(cnt)