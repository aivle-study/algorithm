#문자열 뒤집기
s=input()
num=list(s)
zero=num.count('0')
one=num.count('1')
count=0
if zero>one:
    num=num
    for i in range(len(num)):
        if num[i]=='0':
            if num[i+1]=='0':
                count+=1
                num[i]='1'
                num[i+1]='1'
            else:
                num[i]='1'
                count+=1
else:
    #뒤집기
    num2=[]
    for i in range(len(num)):
        if num[i]=='0':
            num[i]='1'
        else:
            num[i]='0'
    count+=1
print(count,num)