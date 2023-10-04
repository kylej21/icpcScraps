#not fast enough
import sys
from itertools import permutations
lines = []
def isValid(word):
    length = len(word)
    subs=[]
    for x in range(length-length//2+1):
        subs.append(word[x:x+length//2])
    return subs
for x in sys.stdin:
    lines.append(x.strip())
word=lines[0]
perms = permutations(list(word))
checked=[]
for x in perms:
    if x in checked:
        continue
    else:
        checked.append(x)
    temp = isValid(x)
    if len(temp) == len(set(temp)):
        print(''.join(x))
        exit()
print(-1)
