#369게입
n=input()
count=0
for x in n:
    if x=="3":
        count+=1
        print("clap",end="")
    if x=="6":
        count+=1
        print("clap",end="")
    if x=="9":
        count+=1
        print("clap",end="")
if count==0:
    print(n)
