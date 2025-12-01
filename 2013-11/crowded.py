import sys
sys.stdin = open("crowded.in")
sys.stdout = open("crowded.out", 'w')
from collections import deque
import math

n, d = map(int, input().split())
cows = [tuple(map(int, input().split())) for _ in range(n)]
# location, height
cows.sort()
# print(cows)

# construct the sparse table
heights = [cows[i][1] for i in range(n)]
tables = [heights]
x = 2
idx = 1
while x <= n:
    curList = []
    prevLen = len(tables[idx - 1])
    for i in range(prevLen):
        if i + 2 ** (idx - 1) > prevLen - 1:
            break
        newVal = max(tables[idx - 1][i], tables[idx - 1][i + 2 ** (idx - 1)])
        curList.append(newVal)
    tables.append(curList)
    idx += 1
    x *= 2
# print(tables)

def f(L, R):
    # inclusive range
    numsInSegment = R - L + 1
    power = math.floor(math.log2(R - L))
    return max(tables[power][L], tables[power][L + (numsInSegment - 2 ** power)])

ans = 0
window = deque()
lPtr = 0
rPtr = 0
for i in range(n):
    # update left
    while cows[lPtr][0] < cows[i][0] - d:
        lPtr += 1
    # update right
    if rPtr < n - 1:
        while cows[rPtr + 1][0] <= cows[i][0] + d:
            rPtr += 1
            if rPtr == n - 1:
                break
    # print(lPtr, rPtr)
    # prevent log2(0) --> domain error
    if lPtr < i and i < rPtr:
        leftMax = f(lPtr, i)
        rightMax = f(i, rPtr)

        if leftMax >= 2 * cows[i][1] and rightMax >= 2 * cows[i][1]:
            # print(i)
            ans += 1
print(ans)
'''
trying the sparse table implementation!
other options would be the segment tree & square root decomposition
will look into the latter w/ Mo's algorithm, etc.

idea: sliding window of indices for each cow, O(1) sparse table query & linear traversal
'''