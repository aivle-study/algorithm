# # 사탕나누기
# # (-1) or (+1 -1)

# #차이 절대값 이동

# import numpy as np
# n=int(input())
# a_i=list(map(int,input().split(" ")))
# x=int(np.mean(a_i))
# a_i=sorted(a_i)    
# print(a_i)
# count=0
# while True:
#     for i in range(len(a_i)):
#         if a_i[i]<x :
#             print(a_i[i],x)
#             y=x-a_i[i]
#             a_i[i]+=y
#             a_i[len(a_i)-i-1]-=y
#             count+=y
#             print(a_i)
#             print(y)
#         elif a_i[i]>x:
#             if a_i[i]-x==1:
#                 count+=1
#                 a_i[i]-=1
#                 print(a_i)
#             else:
#                 print(a_i[i],x)
#                 y=a_i[i]-y
#                 a_i[i]+=y
#                 a_i[len(a_i)-i-1]-=y
#                 count+=y
#                 print(y)
#     if len(set(a_i))==1:
#         print('OKAY')
#         print(count)
#         break   
#     break
# print(count)
# # 최대 최소 조합
import numpy as np
n=int(input())
a_i=list(map(int,input().split(" ")))
x=int(np.mean(a_i))
a_i_2=[]
for i in range(len(a_i)):
    a_i_2.append(a_i[i]-x)

# count=0
# while True:
#     check=0
#     for i in range(1,len(a_i_2)):
#         if abs(a_i_2[check])==abs(a_i_2[i])and abs(a_i_2[check])>0 and abs(a_i_2[i])>0:
#             count+=abs(a_i_2[check])
#             a_i_2[check]=0
#             a_i_2[i]=0
#             #print(a_i_2)
#         elif abs(abs(a_i_2[check])-abs(a_i_2[i]))==1 and abs(a_i_2[check])>0 and abs(a_i_2[i])>0:
#             count+=1
#             if a_i_2[check]<0:
#                 a_i_2[check]+=1
#             else:
#                 a_i_2[check]-=1
#             if a_i_2[i]<0:
#                 a_i_2[i]+=1
#             else:
#                 a_i_2[i]-=1
#             #print(a_i_2)
        
#     for i in range(len(a_i_2)):
#         if abs(a_i_2[i])==1:
#             count+=1
#             if a_i_2[i]<0:
#                 a_i_2[i]+=1
#             else:
#                 a_i_2[i]-=1
#             #print(a_i_2)
#         for j in range(i,len(a_i_2)):
#             if a_i_2[i]>0 and a_i_2[j]<0:
#                 if abs(a_i_2[i])>abs(a_i_2[j]):
#                     count+=abs(a_i_2[j])
#                     a_i_2[i]=a_i_2[i]+a_i_2[j]
#                     a_i_2[j]=0
                    
#                 else:
#                     count+=abs(a_i_2[i])
#                     a_i_2[j]=a_i_2[i]+a_i_2[j]
#                     a_i_2[i]=0 
#                 #print(a_i_2)
#                 break
#     break
count=0
for i in range(len(a_i_2)):
    if a_i_2[i]>0:
        count+=a_i_2[i]
print(count)