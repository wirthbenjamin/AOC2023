import numpy as np
import queue
from heapq import heapify, heappush, heappop

dirs = [[-1,0],[0,1],[1,0],[0,-1]]# NOSW

def addt(a,b):
    return (a[0]+b[0],a[1]+b[1]) 
def mult(a,b):
    return (a[0]*b,a[1]*b)
def next(p):
    dist = p[0]
    pos = p[1][0]
    dir = p[1][1]

    xlen = loss.shape[1]
    ylen = loss.shape[0]
    ret = []
    for i in range(4):
        
        if(i==(dir+2) or i== dir-2): # opposite direction
            continue
        if(i==dir):
            continue
        dist = p[0]
        for s in range(1,11):
            nd = mult(dirs[i],s)
            np = addt(pos,nd)
            if(not (0<=np[0]<len(inp) and 0<=np[1]<len(inp[0]))):
                continue
            dist += loss[np]
            if(s>=4):
                ret.append((dist,(np,i)))
    return ret


with open('input.txt') as file:
    inp = file.read().split("\n")

loss=[]
for line in inp:
    loss.append([])
    for c in line:
        loss[-1].append(int(c))

loss = np.array(loss)

straight = 0
dist={}
prev = {}
q = [(0,((0,0),-10))] # dist, ((pos),(dir),straight)
dist[q[0]] = 0#loss[0,0]
heapify(q)

while(q):
    node = heappop(q)
    nextnodes = next(node)
    for n in nextnodes:
        if(n[1][0]==(len(inp)-1,len(inp[0])-1)):
            print(n)
        if(n[1] not in dist):
            dist[n[1]]=n[0]
            prev[n[1]]=node
            heappush(q,n)
        else:
            if n[0] < dist[n[1]]:
                dist[n[1]]=n[0]
                prev[n[1]]=node
                heappush(q,n)
losses = []  
for i in range(4):
    if ((len(inp)-1,len(inp[0])-1),i)in dist:
        print(dist[((len(inp)-1,len(inp[0])-1),i)])
