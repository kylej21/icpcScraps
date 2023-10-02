import sys
inp = []
for x in sys.stdin:
    inp.append(x.strip())
totalLines = int(inp[0].split(" ")[1]) * 5
inp.pop(0)
nums=[]
totalNum = 0
for x in inp:
    nums.append(int(x))
for x in sorted(nums):
    if totalLines >= x:
        totalLines -= x
        totalNum +=1
print(totalNum)