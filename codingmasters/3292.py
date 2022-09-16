H,W=map(int,input().split())
back=[list(input()) for i in range(H)]
h,w=map(int,input().split())
people=[input() for i in range(h)]
new_back=[]
later_h=[]
later_w=[]
for i in range(h):
    new_back.append(back[H-h:][i][W-w:])
    #later_h.append(back[:H-h])
    later_w.append(back[H-h:][i][:W-w])
#print(new_back)
for i in range(h):
    for j in range(w):
        if people[i][j]!='.':
            new_back[i][j]=people[i][j]
new_back2=[]
for i in range(h):
    new_back2.append(''.join(new_back[i]))
# print(new_back2)
# print(later_w)
new_back3=[]
# print(new_back3)
new_back3.append(''.join(back[W-w-1]))
for i in range(h):
    new_back3.append(later_w[i][0]+new_back2[i])
for i in range(H):
    print(new_back3[i])

            
    