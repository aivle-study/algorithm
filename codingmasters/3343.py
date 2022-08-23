

# # 3: .....,.....,.....,.....,....#
# # 4: '....', '....', '....', '....'


#체크 도입
n=int(input()) #한변의 길이
wall=[input() for i in range(n)]
check=[[0]*n for i in range(n)] #0가능 1불가능
#print(wall)
#print(check)
for i in range(len(wall)):
    for j in range(len(wall)):
        if wall[i][j]=='#':
            check[i][j]=1
#print(check)
count=0
for i in range(len(wall)):
    for j in range(len(wall)-1):
        if wall[i][j]=='.' and check[i][j]==0: #일단 쓸 수 있음
            
            if wall[i][j+1]=='.' and check[i][j+1]==0:
                count+=1
                check[i][j]=1
                check[i][j+1]=1
                
            # if (j+1)==(len(wall)-1):
            #     print(i,j)
            #     if wall[i-2][j+1]=='.'and check[i-2][j+1]==0:
            #         count+=1
            #         check[i-2][j+1]=1
            #         check[i-1][j+1]=1
            

print(count)
#print(check)