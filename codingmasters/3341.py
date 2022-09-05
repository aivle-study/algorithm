arr=input()
arrr=input()


diarrr=[[arrr[0],'0']]
diarr=[[arrr[0],'0']]
for x in arrr:
    if x==diarrr[-1][0]:
        diarrr[-1][1]=str(1+int(diarrr[-1][1]))
    else:
        diarrr.append([x,'1'])
for x in arr:
    if x==diarr[-1][0]:
        diarr[-1][1]=str(1+int(diarr[-1][1]))
    else:
        diarr.append([x,'1'])

count=0
for x in range(10):
    tuff1=0
    tuff2=0
    tuff3=0
    if int(diarrr[0][1])>int(diarr[0][1]):
        tuff1=1
    if int(diarrr[0][1])//int(diarr[0][1])>=2:
        tuff1=2
    if len(diarrr)>1:
        if int(diarrr[1][1])>int(diarr[1][1]):
            tuff2=1
        if int(diarrr[1][1])//int(diarr[1][1])>=2:
            tuff2=2
    if len(diarrr)>2:  
        if int(diarrr[2][1])>int(diarr[2][1]):
            tuff3=1    
        if int(diarrr[2][1])//int(diarr[2][1])>=2:
            tuff3=2
    if tuff1==0 and tuff2==0 and tuff3==0:
        break
    if (tuff1==2 and tuff2==2 and (tuff3==2 or tuff3==1)) or ((tuff1==2 or tuff1==1) and tuff2==2 and tuff3==2) or (tuff1==1 and tuff2==2 and tuff3==1):
        diarr[0][1]=str(int(diarr[0][1])*2)
        diarr[1][1]=str(int(diarr[1][1])*2)
        diarr[2][1]=str(int(diarr[2][1])*2)
        count+=1
        continue
    if (tuff1==2 or tuff1==1) and (tuff2==1 or tuff2==2):
        diarr[0][1]=str(int(diarr[0][1])*2)
        diarr[1][1]=str(int(diarr[1][1])*2)
        count+=1
        continue
    if (tuff2==1 or tuff2==2) and (tuff3==1 or tuff3==2):
        diarr[1][1]=str(int(diarr[1][1])*2)
        diarr[2][1]=str(int(diarr[2][1])*2)
        count+=1
        continue
    if tuff1==2 or tuff1==1:
        diarr[0][1]=str(int(diarr[0][1])*2)
        count+=1
        continue
    if tuff2==2 or tuff2==1:
        diarr[1][1]=str(int(diarr[1][1])*2)
        count+=1
        continue
    if tuff3==2 or tuff3==1:
        diarr[2][1]=str(int(diarr[2][1])*2)
        count+=1
        continue

print(count)