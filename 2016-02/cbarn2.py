import sys
sys.stdin = open("cbarn.in")
sys.stdout = open("cbarn.out", 'w')
from collections import deque

n = int(input())
cows = [int(input()) for _ in range(n)]
# print(cows)

def checkStart(startIdx):
    c = cows.copy()
    q = deque([])
    cost = 0
    for i in range(n):
        idx = (startIdx + i) % n
        for _ in range(cows[idx]):
            q.append(i)
        if not q:
            return float('inf')
        j = q.popleft()
        cost += (i - j) ** 2
    return cost

ans = float('inf')
for i in range(n):
    # try starting at every point
    ans = min(ans, checkStart(i))
assert ans != float('inf')
print(ans)

'''
alright, editorial here we go
'''
