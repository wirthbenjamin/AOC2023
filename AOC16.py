with open('input.txt') as file:
    inp = file.read().split("\n")




#(tuple(pos),tuple(dir))
def proc(p, d):
    xlen = len(inp[0])
    ylen = len(inp)
    if(not (0 <= p[0]+d[0] < ylen and 0<=p[1]+d[1]<xlen)):
        return [],[]
    nextp =[p[0]+d[0],p[1]+d[1]]
    next = inp[p[0]+d[0]][p[1]+d[1]]
    if(next == '.'):
        return [nextp],[d]
    elif(next == '|'):
        return [nextp,nextp],[[1,0],[-1,0]]
    elif(next=='-'):
        return [nextp,nextp],[[0,1],[0,-1]]
    elif(next == '/'):
        return [nextp] , [[-d[1],-d[0]]]
    elif(next=='\\'):
        return [nextp], [[d[1],d[0]]]


visited = set()
seen = set() 
pos = [[0,-1]]
dir = [[0,1]]
while pos:
    if((tuple(pos[0]),tuple(dir[0])) in seen):
        pos.remove(pos[0])
        
        dir.remove(dir[0])
        continue
    else:
        seen.add((tuple(pos[0]),tuple(dir[0])))
        visited.add(tuple(pos[0]))
        [p,d] = proc(pos[0],dir[0])
        for i in range(len(p)):
            pos.append(p[i])
            dir.append(d[i])
print(len(visited)-1)

maxcount = 0

slen = [len(inp[0]),len(inp),len(inp[0]),len(inp)]
sdir = [[1,0],[0,1],[-1,0],[0,-1]]
for i in range(4):# top, left, bot, right
    

    for j in range(slen[i]):
        spos = [[-1,j],[j,-1],[len(inp),j],[j,len(inp[0])]]
        
        visited = set()
        seen = set() 
        pos=[spos[i]]
        dir=[sdir[i]]
        while pos:
            if((tuple(pos[0]),tuple(dir[0])) in seen):
                pos.remove(pos[0])
                
                dir.remove(dir[0])
                continue
            else:
                seen.add((tuple(pos[0]),tuple(dir[0])))
                visited.add(tuple(pos[0]))
                [p,d] = proc(pos[0],dir[0])
                for k in range(len(p)):
                    pos.append(p[k])
                    dir.append(d[k])
        maxcount= max(maxcount,len(visited)-1)
        
print(maxcount)
