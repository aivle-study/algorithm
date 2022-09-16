#왕실의 나이트
# 수평 두칸  수직 한칸
# 수직 두칸 수평 한칸
status=input()
steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)] #행열 순
row=int(status[1]) #행
col=int(ord(status[0]))-int(ord('a'))+1 #열
count=0
for step in steps:
    n_row=row+step[0]
    n_col=col+step[1]
    if n_row>=1 and n_row<=8 and n_col>=1 and n_col<=8:
        count+=1
print(count)