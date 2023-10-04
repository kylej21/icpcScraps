#not fast enough
import sys
lines = []
def isValid(word):
    length = len(word)
    subs=[]
    for x in range(length-length//2+1):
        subs.append(word[x:x+length//2])
    if len(subs) == len(set(subs)):
        return True
    else:
        return False
for x in sys.stdin:
    lines.append(x.strip())
word=lines[0]

def permutations(head, tail=''):
    if len(head) == 0:
        if isValid(tail):
            print(tail)
            exit()
    else:
        for i in range(len(head)):
            permutations(head[:i] + head[i+1:], tail + head[i])

permutations(word)
print(-1)