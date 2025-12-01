import sys
sys.stdin = open("nocow.in")
sys.stdout = open("nocow.out", 'w')
from collections import defaultdict

n, k = map(int, input().split())
lines = [list(input().split())[4:-1] for _ in range(n)]
# print(lines)
traits = len(lines[0])
categories = [set() for _ in range(traits)]
for i in range(n):
    for j in range(traits):
        categories[j].add(lines[i][j])

traitToIdx = defaultdict(int)
for i in range(traits):
    categories[i] = sorted(list(categories[i]))
    for j in range(len(categories[i])):
        traitToIdx[categories[i][j]] = j
# print(categories)
# print(traitToIdx)

mx = 1
for category in categories:
    mx *= len(category)

cowIdx = []
for line in lines:
    cowNumber = 0
    multiplier = mx
    for i in range(traits):
        multiplier //= len(categories[i])
        cowNumber += multiplier * traitToIdx[line[i]]
        # print(multiplier, traitToIdx[line[i]])
    cowIdx.append(cowNumber)
cowIdx.sort()
# print(cowIdx)

trueK = k - 1
for c in cowIdx:
    if c <= trueK: trueK += 1
# print(trueK)

# like we would with digits
i = 0
multiplier = mx
ans = []
for i in range(traits):
    # converge on trueK
    multiplier //= len(categories[i])
    x = trueK // multiplier
    trueK %= multiplier
    ans.append(categories[i][x])
print(*ans)
'''
permutation problem w/ a twist
missing elements
fast-forward to normal k value, then go one more for each missing
n < 100 so we can iteratively go through the missing cows

ex. 1, 3, 5, 7, 9, k=4
k   real
4    2
5    2
6    3
7    3
8    4
--> now reverse-engineer from here

1. determine indices of current cows
2. adjust k to real value
3. get the name of the new k
'''
