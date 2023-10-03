import sys
inp = []
for x in sys.stdin:
    inp.append(x.strip())
realInp = inp[0].split(" ")
target = int(realInp[0])
maxPer = int(realInp[1])
maxNum = int(realInp[2])
sols=[]
import math
divs = [1]
for i in range(2,int(math.sqrt(target))+1):
    if target%i == 0:
        divs.extend([i,target//i])
divs.extend([target])
divs = sorted(list(set(divs)))
for x in divs:
    if x > maxPer:
        continue
    elif (target+x-1)//x > maxNum:
        continue
    else:
        sols.append(x)
print(len(sols))
for x in sorted(sols):
    print(x)
