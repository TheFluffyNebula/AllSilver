import sys
sys.stdin = open('trapped.in')
sys.stdout = open('trapped.out', 'w')

'''
sort bales on position
for each haybale, LOCK it as if it's the haybale that holds w/o any help

WLOG, 
for each haybale on LEFT, 
based on bale strength, find the highest strength bale within bale_loc + bale_size
strength = bale_loc + size (how far it covers)
use prefix maximum
since we don't have exact locations, binary search. 
'''

n, b = map(int, input().split())
leftBales = []
rightBales = []
for i in range(n):
    size, position = map(int, input().split())
    if position < b:
        leftBales.append((position, size))
    else:
        rightBales.append((position, size))
leftBales.sort()
rightBales.sort()
# print(leftBales, rightBales)

leftC = len(leftBales)
rightC = len(rightBales)
if leftC == 0 and rightC == 0:
    print(-1)
    exit()

# higher is better
leftPf = [0] * leftC
# lower is better
rightPf = [float('inf')] * rightC
cur = 0
for i in range(leftC - 1, -1, -1):
    cur = max(cur, leftBales[i][0] + leftBales[i][1])
    leftPf[i] = cur
cur = float('inf')
for i in range(rightC):
    cur = min(cur, rightBales[i][0] - rightBales[i][1])
    rightPf[i] = cur
# print(leftPf, rightPf)

# first iteration: (1, 8) --> need something within 9
# (8, 3) within 9, currently reaches to 5, extra 4 to get to reach 1
best = float('inf')
for i in range(leftC):
    within = leftBales[i][0] + leftBales[i][1]
    if within <= b:
        continue
    L = 0
    R = rightC - 1
    idx = -1
    while L <= R:
        mid = (L + R) // 2
        if rightBales[mid][0] <= within:
            idx = mid
            L = mid + 1
        else:
            R = mid - 1
    if idx == -1:
        continue
    coversTo = rightPf[idx]
    best = min(best, max(0, coversTo - leftBales[i][0]))

for i in range(rightC):
    within = rightBales[i][0] - rightBales[i][1]
    if within >= b:
        continue
    L = 0
    R = leftC - 1
    idx = -1
    while L <= R:
        mid = (L + R) // 2
        if leftBales[mid][0] >= within:
            idx = mid
            R = mid - 1
        else:
            L = mid + 1
    if idx == -1:
        continue
    coversTo = leftPf[idx]
    best = min(best, max(0, rightBales[i][0] - coversTo))
print(-1) if best == float('inf') else print(best)
