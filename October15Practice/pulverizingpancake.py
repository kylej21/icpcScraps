import sys
lines = []
for x in sys.stdin:
    lines.append(x.strip())
pokNums= lines[0].split(" ")
profs=[int(x) for x in[*lines[1]]]
slams=0
for i in range(len(profs)):
    if profs[i]==0:
        continue
    else:
        profs[i]=0
        if i< len(profs)-2:
            profs[i+2] += profs[i+1]
            profs[i+1]=0
        slams+=1
print(slams)