import sys
inp = []
for x in sys.stdin:
    inp.append(x.strip())
first = int(inp.pop(0))

inp = [list(map(int, x.split())) for x in inp]

inp = [range(x[0], x[1]+1) for x in inp]



print(inp)
idx=0
pairs=0
while idx<len(inp)-2:
    for x in inp[idx]:
        print(x)
        if(x in inp[idx+1] and x in inp[idx+2]):
            pairs+=1
            inp = inp[3:]
        else:
            idx+=1        
print(pi)