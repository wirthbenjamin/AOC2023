with open('input.txt') as file:
    inp = file.read().split("\n")

import shapely as sh
import numpy as np
from shapely.geometry import Polygon

dirs={'U':np.array([1,0]),'R':np.array([0,1]),'D':np.array([-1,0]),'L':np.array([0,-1])}

coords=[]
pos = np.array((0,0))
for line in inp:
    c = line.split(' ')
    d = dirs[c[0]]
    s= int(c[1])
    coords.append(pos)
    pos = pos+s*d


a = Polygon(coords)

print(a.buffer(0.5,join_style='mitre').area)

dirs={'0':np.array([1,0]),'1':np.array([0,1]),'2':np.array([-1,0]),'3':np.array([0,-1])}

coords=[]
pos = np.array((0,0))
for line in inp:
    c = line.split(' ')
    d = dirs[c[2][7]]
    s= int(c[2][2:7],16)
    coords.append(pos)
    pos = pos+s*d


a = Polygon(coords)

print(a.buffer(0.5,join_style='mitre').area)
