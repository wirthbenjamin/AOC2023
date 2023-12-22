with open('input.txt') as file:
    inp = file.read().split('\n')

def addt(a,b):
    return (a[0]+b[0],a[1]+b[1])
stones = set()
start = (0,0)
for i,line in enumerate(inp):
    for j,c in enumerate(line):
        if(c == '#'):
            stones.add((i,j))
        if(c == 'S'):
            start = (i,j)

def inbounds(pos):
    return 0<=pos[0]<len(inp) and 0<=pos[1]<len(inp[0])
def mod(pos):
    return (pos[0]%len(inp),pos[1]%len(inp))

dirs = ((-1,0),(1,0),(0,-1),(0,1))
nextp = set()
nextp.add(start)

for i in range(64):
    current=nextp
    nextp = set()
    for pos in current:
        for d in dirs:
            c = addt(pos,d)
            if(inbounds(c)):
                if(c not in stones):
                    nextp.add(c)
print(len(nextp))

nextp = set()
current = set()
last = set()
nextp.add(start)
hits = []
hist = []
new = []
dnew = []
evenhits = 0
oddhits = 1

t = 26501365


for i in range(5*len(inp)):
    last = current
    current=nextp
    nextp = set()
    for pos in current:
        for d in dirs:
            c = addt(pos,d)
            if(mod(c) not in stones and c not in last and c not in nextp):
                nextp.add(c)
                if(i%2):
                    oddhits += 1
                    
                else:
                    evenhits +=1
    if(i%2):
        #print(f'{i} - {oddhits}')
        hits.append(oddhits)
    else: 
        #print(f'{i} - {evenhits}')
        hits.append(evenhits)
    if((i+1)%len(inp) == t%len(inp)):
        hist.append(hits[-1])


d1 = [a-b for a,b in zip(hist[1:],hist)]
d2 = [a-b for a,b in zip(d1[1:],d1)]
buf = t//len(inp)
n = buf-len(hist)+1
print(hist[-1] + d1[-1]*n+d2[-1]*n*(n+1)/2)
pass
'''
t = 5000

for i in range(50):
    new.append(0)
    last = current
    current=nextp
    nextp = set()
    for pos in current:
        for d in dirs:
            c = addt(pos,d)
            if(mod(c) not in stones and c not in last and c not in nextp):
                nextp.add(c)

                hits+=1
                new[-1]+=1
    if((i+1)%len(inp)==t%len(inp)):
        print(hits)
        hist.append(hits)
    if(i>1):
        print(f'{i+1} {hits}')

print(hist)
buf=[a-b for a,b in zip(hist[1:],hist)]
print(buf)
d1 = buf[-1]
buf = [a-b for a,b in zip(buf[1:],buf)]
d2 = buf[-1]
print(buf)
a=t//len(inp)
n=len(hist)
print(hist[-1]+d1*n+d2*n*(n+1)/2)
pass
'''