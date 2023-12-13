with open(r'D:\Python\AOC23\input.txt') as file:
    inp = file.read().split("\n")

cards = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}
jokercards = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':0,'Q':11,'K':12,'A':13}
inv_map = {}
for k, v in jokercards.items():
    inv_map[v] = k
class jokerhand:
    def __init__(self,istr):
        self.bid=int(istr.split(' ')[1])
        self.cards=istr.split(' ')[0]
        self.jokers=self.cards.count('J')
        self.freq=[0 for a in cards]
        for c in self.cards:
            if(c!='J'):
                self.freq[jokercards[c]]+=1
        maxoccur= inv_map[self.freq.index(max(self.freq))]
        if(maxoccur=='J'):
            maxoccur='A'
        self.jcards = self.cards
        self.jcards = self.jcards.replace('J',maxoccur)
        self.types=[0,0,0,0,0]
        self.freq=[0 for a in cards]
        for c in self.jcards:
            if(c!='J'):
                self.freq[jokercards[c]]+=1
        for f in self.freq:
            if(f>0):
                self.types[f-1]+=1
        if(self.types==[5,0,0,0,0]):
            self.type=0
        elif(self.types==[3,1,0,0,0]):
            self.type=1
        elif(self.types==[1,2,0,0,0]):
            self.type=2
        elif(self.types==[2,0,1,0,0]):
            self.type=3
        elif(self.types==[0,1,1,0,0]):
            self.type=4
        elif(self.types==[1,0,0,1,0]):
            self.type=5
        elif(self.types==[0,0,0,0,1]):
            self.type=6
        else:
            pass
    def __repr__(self):
        return self.cards
    def __lt__(self,other):
        if(other.type>self.type):
            return True
        elif(other.type==self.type):
            for i in range(5):
                if(jokercards[other.cards[i]]>jokercards[self.cards[i]]):
                    return True
                elif(jokercards[other.cards[i]]<jokercards[self.cards[i]]):
                    return False
        return False
class hand:
    def __init__(self,istr):
        self.bid=int(istr.split(' ')[1])
        self.cards=istr.split(' ')[0]
        self.freq=[0 for a in cards]
        for c in self.cards:
            self.freq[cards[c]]+=1
        self.types=[0,0,0,0,0]
        for f in self.freq:
            if(f>0):
                self.types[f-1]+=1
        if(self.types==[5,0,0,0,0]):
            self.type=0
        elif(self.types==[3,1,0,0,0]):
            self.type=1
        elif(self.types==[1,2,0,0,0]):
            self.type=2
        elif(self.types==[2,0,1,0,0]):
            self.type=3
        elif(self.types==[0,1,1,0,0]):
            self.type=4
        elif(self.types==[1,0,0,1,0]):
            self.type=5
        elif(self.types==[0,0,0,0,1]):
            self.type=6
        else:
            pass
    def __repr__(self):
        return self.cards
    def __lt__(self,other):
        if(other.type>self.type):
            return True
        elif(other.type==self.type):
            for i in range(5):
                if(cards[other.cards[i]]>cards[self.cards[i]]):
                    return True
                elif(cards[other.cards[i]]<cards[self.cards[i]]):
                    return False
        return False
    

hands = [jokerhand(l) for l in inp]

tot = 0
for i,h in enumerate(sorted(hands)):
    tot+=(i+1)*h.bid

print(sorted(hands))
print(tot)
