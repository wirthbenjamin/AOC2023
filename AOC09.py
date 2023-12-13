with open(r'D:\Python\AOC23\input.txt') as file:
    inp = file.read().split('\n')
numinp = []
for line in inp:
    numinp.append(list(map(int,line.split())))
tot = 0
tot2 = 0
for nums in numinp:
    i=0
    d=nums
    lastd=[d[-1]]
    firstd=[d[0]]
    while([True for n in d if(n!=0)]):
        buf=[b-a for a,b in zip(d[0:-1],d[1:])]
        d=buf
        i+=1
        lastd.append(d[-1])
        firstd.append(d[0])
    tot2 += sum(firstd[0::2])-sum(firstd[1::2]) 
    tot+=sum(lastd)

print(tot)
print(tot2)