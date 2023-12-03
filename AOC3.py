import numpy as np
import scipy as sp

with open('input.txt') as file:
    inp = file.read().split("\n")

schema = inp
symbols = np.zeros((len(inp),len(inp[0])))
numbers = np.zeros((len(inp),len(inp[0])))
stars = np.zeros((len(inp),len(inp[0])))
for i,line in enumerate(inp):
    for j,char in enumerate(line):
        if(char.isdigit()):
            numbers[i,j] = 1
        elif(char!='.'):
            if(char=='*'):
                stars[i,j]=1
            symbols[i,j]=1

symboladj = sp.signal.convolve2d(symbols,[[1,1,1],[1,0,1],[1,1,1]],mode = 'same')>=1


total = 0
for i,line in enumerate(inp):
    value = 0
    add = False
    for j,char in enumerate(line):
        
        if(char.isdigit()):
            value = value*10+int(char)
            if(symboladj[i,j]):
                add=True
        else:
            if(add):
                total += value
            value=0
            add = False
    if(add):
        total += value
starmap = {}
for i,line in enumerate(inp):
    star = (0,0)
    
    value = 0
    for j,char in enumerate(line):
        if(char.isdigit()):
            value = value*10+int(char)
            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    if(0<=i+k<len(inp) and 0<j+l<len(inp[0])):
                        if(stars[i+k,j+l]):
                            star = (i+k,j+l)
        if(not char.isdigit()):
            if(star != (0,0)):
                if(not star in starmap):
                    starmap[star]=[value]
                else:
                    starmap[star].append(value)
                
            star = (0,0)
            value = 0
    if(star != (0,0)):
        if(not star in starmap):
            starmap[star]=[value]
        else:
            starmap[star].append(value)

print(total)
print(sum([starmap[a][0]*starmap[a][1] for a in starmap if(len(starmap[a])==2)]))
