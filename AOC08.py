from math import lcm
with open(r'D:\Python\AOC23\input.txt') as file:
    inp = file.read()

moves = inp.split('\n\n')[0]
locs_str = inp.split('\n')[2:]

locs={}
for loc in locs_str:
    n=tuple(loc[0:3])
    l=tuple(loc[7:10])
    r=tuple(loc[12:15])
    locs[n]={'L':l,'R':r}

loc = locs[tuple('AAA')]

i = 0

while loc!=locs[tuple('ZZZ')]:
    loc = locs[loc[moves[i%len(moves)]]]
    
    i+=1
print(i)
starts = [locs[a] for a in locs.keys() if(a[-1]=='A')]
freq = [[] for a in starts]

for s,loc in enumerate(starts):
    c=0
    i=0
    j=0
    while c<3:
        next = loc[moves[i%len(moves)]]
        loc=locs[next]
        if(next[-1]=='Z'):
            freq[s].append(j)
            j=0
            c+=1
        i+=1
        j+=1
print(freq)
done=False
print(lcm(freq[0][1],freq[1][1],freq[2][1],freq[3][1],freq[4][1],freq[5][1]))

'''
curlocs = starts
names = [loc[moves[i%len(moves)]]for loc in curlocs]
while [True for a in names if(a[-1]!='Z')]:
    names = [loc[moves[i%len(moves)]]for loc in curlocs]
    curlocs = [locs[loc[moves[i%len(moves)]]] for loc in curlocs]
    i+=1
print(i)

'''
