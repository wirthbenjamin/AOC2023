class mapping:
    def __init__(self,initstr):

        self.start = 0
        self.length = 0
        self.target = 0

        #arget start length
        [self.target, self.start, self.length] = [int(a) for a in initstr.split(' ')]
    def isinside(self, seed):
        if(self.start<seed<self.start+self.length):
            return True
        return False
    def get_target(self,seed):
        if( self.isinside(seed)):
            return seed-self.start+self.target
        else:
            return -1
    def get_ranges(self,mapped, unmapped):
        unmappedbuf = []
        while(len(unmapped)!= 0):
            buf = unmapped.pop()
            start = buf[0]
            length= buf[1]

            
            
            bm = self.start
            em = self.start+self.length-1
            bs = start
            es = start+length-1
            if(bs<bm and es<bm):
                unmappedbuf.append([bs,length])
            elif(bs<bm and bm<=es<=em):
                unmappedbuf.append([bs, bm-bs])
                mapped.append([self.target,length-(bm-bs)])
            elif(bs<bm and em<es):
                unmappedbuf.append([bs,bm-bs])
                unmappedbuf.append([em+1,es-em])
                mapped.append([self.target,self.length])
            elif(bm<=bs<=em and bm<=es<=em):
                mapped.append([self.target+bs-bm,length])
            elif(bm<=bs<=em and em<es):
                mapped.append([self.target+bs-bm,em-bs+1])
                unmappedbuf.append([em+1, es-em])    
            elif(em<bs):
                unmappedbuf.append([bs,length])         
            else:
                pass
        return mapped,unmappedbuf
        
def get_target(maps,source):
    for map in maps:
        a = map.get_target(source)
        if(a!=-1):
            return a
    return source
        
with open(r'D:\Python\AOC23\input.txt') as file:
    inp = file.read().split("\n\n")

seeds = [int(a) for a in inp[0].split()[1:]]
maps = []
for block in inp[1:]:
    maps.append([])
    for line in block.split('\n')[1:]:
        maps[-1].append(mapping(line))

for mappings in maps:
    seeds = [get_target(mappings,a) for a in seeds]

print(min(seeds))

seedranges = [[int(a), int(b)] for a,b in zip(inp[0].split()[1::2],inp[0].split()[2::2])]

for mappings in maps:
    unmapped = []
    mapped = []
    unmapped=seedranges
    for map in mappings:
        mapped,unmapped = map.get_ranges(mapped,unmapped)
            
            
    seedranges = mapped + unmapped
print(min([a[0]for a in seedranges]))