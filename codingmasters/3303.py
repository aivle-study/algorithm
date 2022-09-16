#최소는 고려할게 없음, 최대는 최소까지 고려해야함
a,b,D,d=map(int,input().split(" "))
min_count=1
min_count2=0
A=a
B=b
#최소 고려
while a>=d:
    if a-d>=d:
        a=a-d
        min_count+=1
    else:
        min_count*=2
        if A==b:
            min_count*=2
        else: 
            min_count2=1
            while b>=d:
                if b-d>=d:
                    b=b-d
                    min_count2+=1
                else:
                    min_count2*=2
                    break
        break
min=min_count+min_count2

#최대
max_count1=1
max_count2=0
a=A
while a>=d:
    if a-D>D and a-D>=d: #최대거리보다 넘으면 안뎅
        a=a-d
        max_count1+=1
    elif a-D>=d:
        a=a-D
        max_count1+=1
    else:
        max_count1*=2
        if A==b:
            max_count1*=2
        else:
            max_count2=1
            b=B
            while b>=d:
                if b-D>=d:
                    b=b-D
                    max_count2+=1
                elif b-D>D and b-D>=d:
                    b=b-d
                    max_count2+=1
                else:
                    max_count2*=2
                    break
        break
print(max_count1+max_count2,min)