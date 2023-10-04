#not fast enough
import sys
lines = []
for x in sys.stdin:
    lines.append(int(x.strip()))
del lines[0]
nums=[]
for x in lines:
    initNum=x
    oldLen = len(nums)
    while oldLen == len(nums):
        if initNum not in nums:
            nums.append(initNum)
        else:
            initNum= initNum + x
    print(initNum)
