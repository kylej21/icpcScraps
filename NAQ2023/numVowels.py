#Description:
#This program inputs a string and counts the number of vowels two times - once including y and once excluding
#
import sys
inp = []
for x in sys.stdin:
    inp.append(x.strip())
totalwithout = 0
vowels = ['a','e','i','o','u']
for vowel in vowels:
    totalwithout += inp[0].count(vowel)
totalwith = totalwithout + inp[0].count('y')
print(str(totalwithout) + " " + str(totalwith))