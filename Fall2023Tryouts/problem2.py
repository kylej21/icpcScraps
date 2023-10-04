import sys
lines = []
for x in sys.stdin:
    lines.append(int(x.strip()))
lines.pop()
for x in lines:
    i=11
    while True:
        temp2=[*str(x)]
        temp3=[*str(i*x)]
        temp4 = [int(x) for x in temp2]
        temp5 = [int(x) for x in temp3]
        if sum(temp4) == sum(temp5):
            print(i)
            break
        i+=1