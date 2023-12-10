with open(r'D:\Python\AOC23\input.txt') as file:
    inp = file.read().split('\n')
'''
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is start
'''
import numpy as np
'''right down left up'''
pipemap = {0:np.array(((-1,0),(1,0))),1:np.array(((0,-1),(0,1))),2:np.array(((-1,0),(0,1))),
           3:np.array(((-1,0),(0,-1))),4:np.array(((0,-1),(1,0))),
           5:np.array(((0,1),(1,0))),6:np.array(((0,1),(1,0),(0,-1),(-1,0))),7:np.array(())}

pipemapnum = {'|':0,'-':1,'L':2,
           'J':3,'7':4,'F':5,'S':6,'.':7}

directions = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}

pipes = [[pipemapnum[c] for c in line] for line in inp]
pipes = np.array(pipes)
dist = -np.ones((len(pipes),len(pipes[0])))
xmin = 0
xmax =len(pipes[0])
ymin = 0
ymax = len(pipes)

start = np.where(pipes == 6)
start = np.array((start[0][0],start[1][0]))
cur = tuple(start)
dist[cur]=0
done = False
lastdir = np.array((0,0))
while not done:
    for dir in pipemap[pipes[cur]]:
        if(np.all(dir == -lastdir)):
            continue
        
        cand = tuple(cur+dir)
        if(not (xmin<=cand[1]<xmax,ymin<=cand[0]<ymax)):
            continue
        if(cand == tuple(start)):
            done = True
            break
        if(dist[cand]!=-1):
            continue
        if(-dir in pipemap[pipes[cand]]):
            val = dist[cur]
            cur=cand
            dist[cand] = val+1
            lastdir = dir
            break
        


print((np.max(dist)+1)/2)

tot = 0
for i in range(ymax):
    for j in range(xmax):
        crossings = 0
        lastd=-np.inf
        if(dist[i,j]!=-1):
            continue
        for k in range(xmax):
            if(not (xmin<=j+k<xmax and ymin<=i+k<ymax)):
                break
            if(dist[i+k,j+k]!=-1):
                if(pipes[i+k,j+k] != pipemapnum['7'] and pipes[i+k,j+k]!= pipemapnum['L']):
                    crossings +=1
                
        if(crossings%2 and crossings != 0):
            tot+=1

print(tot)




