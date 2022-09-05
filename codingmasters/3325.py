maps=list(input())
maps2=maps.copy()
for x in range(1,len(maps)):
    if maps[x]=='x':
        if maps[x-1]=='o':
            maps[x]='o'
        else:
            maps[x]='g'

maps="".join(maps)
print(maps.count('og'))
maps=maps2
for x in range(1,len(maps)):
    if maps[x]=='x':
        if maps[x-1]=='o':
            maps[x]='g'
        else:
            maps[x]='o'
maps="".join(maps)
print(maps.count('og'))

