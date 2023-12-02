import re


with open('input.txt') as file:
    inp = file.read().split("\n")

colors = {"red":12,"green":13,"blue":14}

acc = 0
acc2=0
for i,line in enumerate(inp):
    red = []
    g=[]
    bl=[]
    sublines = line.split(';')
    for l in sublines:
        red.append( sum([int(a) for a in re.findall(r'(\d+) red',l)]))
        g.append( sum([int(a) for a in re.findall(r'(\d+) green',l)]))
        bl.append( sum([int(a) for a in re.findall(r'(\d+) blue',l)]))
        

    if(max(red)<=12 and max(g) <= 13 and max(bl)<=14):
        acc+=i+1
    acc2+=max(red)*max(g)*max(bl)
print(acc)
print(acc2)