import numpy as np
import queue
from heapq import heapify, heappush, heappop

dirs = [[-1,0],[0,1],[1,0],[0,-1]]# NOSW

def addt(a,b):
    return (a[0]+b[0],a[1]+b[1]) 
def next(p):
    dist = p[0]
    pos = p[1][0]
    dir = p[1][1]
    st = p[1][2]
    xlen = loss.shape[1]
    ylen = loss.shape[0]
    ret = []
    for i in range(4):
        nd = dirs[i]
        np = addt(pos,dirs[i])
        if(not (0<=np[0]<len(inp) and 0<=np[1]<len(inp[0]))):
            continue
        if(i==(dir+2)%4): # opposite direction
            continue
        if(i==dir):
            if(st==2):
                continue
            else:
                ret.append((dist+loss[np],(np,i,st+1)))
                continue
        ret.append((dist+loss[np],(np,i,0)))
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
q = [(0,((0,0),1,0))] # dist, ((pos),(dir),straight)
dist[q[0]] = 0#loss[0,0]
heapify(q)

while(q):
    node = heappop(q)
    nextnodes = next(node)
    for n in nextnodes:
        if(n[1][0]==(len(inp)-1,len(inp[0])-1)):
            print(n)
            break
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


