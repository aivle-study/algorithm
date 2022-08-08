a=input()
nob=0
for x in a:
    if x=='3' or x=='6' or x=='9':
        print("clap",end="")
        nob=1
if nob==0:
    print(int(a))