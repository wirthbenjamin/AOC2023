with open('input.txt') as file:
    inp = file.read().replace('.','0').replace('#','1').split("\n\n")


vert = [] 
hor = []

def palindrome(nums,sec):
    l = len(nums)
    a=nums[:int(l/2)]
    b=nums[int(l/2):]
    b.reverse()
    if(not sec):
        if(a == b):
            return True
    else:
        if(almosteq(a,b)):
            return True
    return False

def findref(nums,sec = False):
    #slice beginnings check palindrome
    for i in range(1,len(nums)):
        if((len(nums[i:])+1)%2 and palindrome(nums[i:],sec)):
            return len(nums)/2+i/2
        if((len(nums[:i])+1)%2 and palindrome(nums[:i],sec)):
            return i/2
    return 0
def almosteq(s,o):
    diff = 0
    for i, n in enumerate(s):
        if(o[i]!=n):
            if(diff==0):
                diff = o[i]^n
            else:
                return False
    if(bin(diff).count('1')==1):
        return True
    return False

for s in inp:
    s=s.splitlines()
    vert.append([])
    hor.append([])
    for i in range(len(s)):
        hor[-1].append(int(s[i].strip(),2))
    for i in range(len(s[0])):
        b=''
        for j in range(len(s)):
            b+=s[j][i]
        vert[-1].append(int(b.strip(),2))

pass
tot=0
for i in range(len(vert)):
    a = findref(vert[i])
    b= 100*findref(hor[i])
    tot += a+b

print(tot)

tot=0
for i in range(len(vert)):
    a = findref(vert[i],True)
    b= 100*findref(hor[i],True)
    tot += a+b
    print(tot)
print(tot)