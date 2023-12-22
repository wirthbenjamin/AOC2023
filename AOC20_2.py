from collections import deque
import math
with open('input.txt') as file:
    inp = file.read().split('\n')




class flipflop:
    def __init__(self,targets):
        self.state=False
        self.targets = targets
    def registersender(self,sender):
        pass
    def call(self,sender, pulse):
        if(not pulse):
            self.state = not self.state
            return self.state
        
class conjunction:
    def __init__(self,targets):
        self.targets = targets
        self.state ={}
    def registersender(self,sender):
        self.state[sender]=False
    def call(self,sender,pulse):
        self.state[sender]=pulse
        if(all(self.state.values())):
            return False
        else:
            return True


broadcaster = []
modules = {}
for line in inp:
    name = line.split(' ')[0][1:]
    targets = line.split('->')[1].replace(' ', '').split(',')
    if(line.startswith('broadcaster')):
        broadcaster = targets
    if(line.startswith('%')):
        modules[name]= flipflop(targets)
    if(line.startswith('&')):
        modules[name]= conjunction(targets)



for module in modules:
    targets = modules[module].targets
    for t in targets:
        if(t in modules):
            modules[t].registersender(module)
        else:
            out = t

signals = deque()

lows = 0
highs = 0
outc = 0
first={}
next={a:False for a in ['vk','pm','dl','ks']}
i=0
seen = set()
while not len(first)==4:
    i+=1
    lows +=1
    outc=0
    countl={a:0 for a in ['vk','pm','dl','ks']}
    counth={a:0 for a in ['vk','pm','dl','ks']}
    
    #={a:0 for a in ['vk','pm','dl','ks']}
    for t in broadcaster:
        lows += 1
        signals.append(('broadcaster',t,False))
    while signals:
        s = signals.popleft() 
        t = s[1]
        if(t != out):
            res = modules[t].call(s[0],s[2])
            for t2 in modules[t].targets:
                c=(t,t2,res)
                if(c[2] is not None):
                    signals.append(c)
                    if(c[2]):
                        highs+=1
                    else:
                        lows+=1
        if(t  == 'dt'):
            if(s[2]):
                counth[s[0]]+=1
            else:
                countl[s[0]]+=1    
        else:
            outc+=1
    for a in counth:
        if(counth[a]):
            if(a not in first):
                first[a]=i
            print(f'{i}:\thigh{counth[a]}\tlow{countl[a]}')
            next[a]=True
        
        
print(highs*lows)

lcm = 1
for a in first:
    lcm = lcm* first[a]//math.gcd(lcm,first[a])
print(lcm)