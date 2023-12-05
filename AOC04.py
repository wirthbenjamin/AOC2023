with open(r'D:\Python\AOC23\input.txt') as file:
    inp = file.read().split("\n")
total=0
numcopies=[1 for i in range(len(inp))]
for i,line in enumerate(inp):
    
    line=line.replace('  ', ' ')
    line=line.replace('  ', ' ')
    parts = line.split('|')
    print(line)
    card = [int(a) for a in parts[0].split(' ')[2:]if a !='']
    winnum = [int(a) for a in parts[1].split(' ') if a!='']
    points = 0
    winners = 0
    for num in card:
        if(num in winnum):
            points*=2
            winners+=1
            numcopies[i+winners]+=numcopies[i]
            if(points==0):
                points=1
    
    total+= points
print(total)
print(sum(numcopies))