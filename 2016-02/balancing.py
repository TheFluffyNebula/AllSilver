import sys
sys.stdin = open("balancing.in")
sys.stdout = open("balancing.out", 'w')
from collections import defaultdict

n = int(input())
xsort = [tuple(map(int, input().split())) for _ in range(n)]
ysort = xsort.copy()
xsort.sort()
ysort.sort(key = lambda x: x[1])
# print(xsort, ysort)

xd = defaultdict(int)
xValToIdx = defaultdict(int)
for i in range(n):
    xd[xsort[i][0]] += 1
for i, (k, v) in enumerate(xd.items()):
    xValToIdx[k] = i
# print(xValToIdx)
yd = defaultdict(int)
yValToIdx = defaultdict(int)
for i in range(n):
    yd[ysort[i][1]] += 1
for i, (k, v) in enumerate(yd.items()):
    yValToIdx[k] = i
# print(yValToIdx)

present = [[0 for _ in range(len(yValToIdx))] for _ in range(len(xValToIdx))]
for i in range(n):
    r = xValToIdx[xsort[i][0]]
    c = yValToIdx[xsort[i][1]]
    present[r][c] = 1
# print(*present, sep='\n')

# let's do x coordinate then y coordinate
pf = [[0 for _ in range(len(yValToIdx) + 1)] for _ in range(len(xValToIdx) + 1)]
for r in range(len(xValToIdx)):
    for c in range(len(yValToIdx)):
        pf[r + 1][c + 1] = (
            pf[r][c + 1]
            + pf[r + 1][c]
            - pf[r][c]
            + present[r][c]
        )
# print(*pf, sep='\n')

def compute_pf(fromX, fromY, toX, toY):
    return (pf[toX][toY]
            - pf[toX][fromY - 1]
            - pf[fromX - 1][toY]
            + pf[fromX - 1][fromY - 1])

best = float('inf')
# iterate 0-xValToIdx.size, 0-yValToIdx.size
for i in range(1, len(xValToIdx) + 1):
    for j in range(1, len(yValToIdx) + 1):
        topleft = compute_pf(1, 1, i, j)
        topright = compute_pf(1, j + 1, i, len(yValToIdx))
        botleft = compute_pf(i + 1, 1, len(xValToIdx), j)
        botright = compute_pf(i + 1, j + 1, len(xValToIdx), len(yValToIdx))
        mx = max(topleft, topright, botleft, botright)
        best = min(best, mx)  
print(best)

'''
prefix sums w/ coordinate compression
move each horizontal, vertical lines up/right 1k steps for O(N^2)

steps to try: a[0] - 1, a[0] + 1, a[1] + 1, ..., a[-1] + 1
in other words, 1 below the first and then 1 above each
use the information we have to calculate for all quadrants
ex. passed x w/ horizontal&vertical, those are bottom left

wait... are the prefix arrays even enough?
ouch, do I even get good information?
waitwaitwait
if I have bot and I have left... I don't see it

nvm, is what I'm looking for 2D prefix sums?
NxN grid, some 0's, some 1's
that definitely works
'''
