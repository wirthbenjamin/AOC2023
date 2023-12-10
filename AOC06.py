with open(r'D:\Python\AOC23\input.txt') as file:
    inp = file.read().split("\n\n")

Times=        [49,     78,     79,     80]
Distances=   [298,   1185,   1066,   1181]
tot=1
for i,time in enumerate(Times):
    wins=0
    for t in range(1,time+1):
        if(Distances[i]<t*(time-t)):
            wins+=1
    if(wins>0):
        tot*=wins

time = 49787980
distance = 298118510661181

    #t*time-t*t-298118510661181=0
    #t²-t*time+distance = 0
a=(time/2+(time*time/4-distance)**(0.5))
b=(time/2-(time*time/4-distance)**(0.5))
print(a)
print(b)
print(a//1-b//1)

print(tot)