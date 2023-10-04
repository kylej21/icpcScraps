import sys
lines = []
for x in sys.stdin:
    lines.append(x.strip())
num = int(lines[0])
while len(str(num)) >1:
    temp = [*str(num)]
    temp2 = [int(x) for x in temp if int(x) != 0]
    newNum=temp2[0]
    #temp2.remove(0)
    temp2.pop(0)
    for x in temp2:
        newNum = newNum* x
    num = newNum
print(num)