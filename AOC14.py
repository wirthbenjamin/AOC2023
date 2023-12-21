import copy

with open('input.txt') as file:
    inp = file.read().split("\n")

#for each col keep track of the last available position and increase to i if # by 0 if . by 1 if 0
raw=[]
for j in range(len(inp)):
    raw.append([])
    for c in inp[j]:
        raw[j].append('#' if c=='#' else '.')

def eval(inp ):
    m = len(inp)
    
    tot = 0
    for i, line in enumerate(inp):
        tot+=(m-i)*line.count('O')
    return tot

def tilt(inp,iter): #0 north 1 west 2 south 3 east
    m = 0
    new=copy.deepcopy(raw)
    ylen = len(inp)
    xlen= len(inp[0])

    posy = [0 if iter==0 else ylen for a in inp[0]]
    posx = [0 if iter ==1 else xlen for a in inp]

    if(iter == 0):
        for i, line in enumerate(inp):
            for j, c in enumerate(line):
                if(c=='#'):
                    posy[j]=i+1
                if(c=='O'):
                    new[posy[j]][j]='O'
                    posy[j]+=1
    if(iter == 1):
        for i, line in enumerate(inp):
            for j, c in enumerate(line):
                if(c=='#'):
                    posx[i]=j+1
                if(c=='O'):
                    new[i][posx[i]]='O'
                    posx[i]+=1
    if(iter == 2):
        for i, line in enumerate(reversed(inp)):
            for j, c in enumerate(line):
                if(c=='#'):
                    posy[j]=i+1
                if(c=='O'):
                    new[ylen-posy[j]-1][j]='O'
                    posy[j]+=1
    if(iter == 3):
        for i, line in enumerate(inp):
            for j, c in enumerate(reversed(line)):
                if(c=='#'):
                    posx[i]=j+1
                if(c=='O'):
                    new[i][xlen-posx[i]-1]='O'
                    posx[i]+=1

    return new
def cycle(inp):
    for i in range(4):
        inp = tilt(inp,i)
    return inp

print(eval(tilt(inp,0)))
seen={}
count = 0
vals = []
done= False
while not done:
    key = tuple((tuple(i) for i in inp))
    if(key not in seen):
        seen[key]=count
        vals.append(eval(inp))
        count +=1
    else:
        done = True
        last = seen[key]
    inp = cycle(inp)


T = (count-last)
print(vals[(1000000000-last)%T+last])

