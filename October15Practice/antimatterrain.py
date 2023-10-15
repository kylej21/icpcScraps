#DP Solution 
import sys
lines = []
for x in sys.stdin:
    lines.append(x.strip())
if int(lines[0]) == 1:
    print(0)
    exit()
maxn= int(lines[0])
temp=lines[1].split(" ")
prices=[int(x) for x in temp]
profs=[0]*maxn
for i in range(0,maxn):
    profs[i]= profs[i-1]
    for j in range(0,i):
        if j>=2:
            profs[i]= max(profs[i],profs[j-2] + prices[i]-prices[j])
        else:
            profs[i] = max(profs[i], prices[i]-prices[j])
print(profs[maxn-1])