import numpy as np
import scipy as sp

with open('input.txt') as file:
    inp = file.read().split("\n")

schema_numbers = -np.ones((len(inp),len(inp[0])))
symbols = np.zeros((len(inp),len(inp[0])))

for i,line in enumerate(inp):
    for j,char in enumerate(line):
        if(char.isdigit()):
            schema_numbers[i,j]  = int(char)
        elif(char!='.'):
            symbols[i,j]==1

symboladj = sp.signal.convolve2d(symbols,[[1,1,1],[1,1,1],[1,1,1]],mode = 'full')




pass





