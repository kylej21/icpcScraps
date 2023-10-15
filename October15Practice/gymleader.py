import sys
lines = []
for x in sys.stdin:
    lines.append(x.strip())
nums=[int(x) for x in lines[0].split(" ")]
rival = nums[1]
allies = dict()
leaders=[0]*nums[0]

for x in range(len(leaders)):
    allies[x+1]=[]
lines.pop(0)
for x in lines:
    temp=[int(y) for y in x.split(" ")]
    temp1= allies[temp[0]]
    temp1.append(temp[1])
    temp2=allies[temp[1]]
    temp2.append(temp[0])
    allies[temp[0]] = temp1
    allies[temp[1]] = temp2
    leaders[temp[0]-1] +=1
    leaders[temp[1]-1] +=1
while 1 in leaders and leaders[rival-1]>1:
    first1= leaders.index(1)
    leaders[first1] = 0
    tempAllies = allies[first1+1]
    for x in tempAllies:
        leaders[x-1]-=1
        temp3 = allies[x]
        temp3.remove(first1+1)
        allies[x]=temp3
if(leaders[rival-1]<=1):
    print("YES")
else:
    print("NO")