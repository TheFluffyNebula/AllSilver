import sys
sys.stdin = open("countcross.in")
sys.stdout = open("countcross.out", 'w')
from collections import defaultdict

n, k, r = map(int, input().split())

roads = defaultdict(int)
for _ in range(r):
    r, c, rPrime, cPrime = map(lambda x: int(x) - 1, input().split())
    roads[(r, c, rPrime, cPrime)] = True
    roads[(rPrime, cPrime, r, c)] = True

locs = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]
# print(locs)

def out(a, b):
    if 0 <= a <= n - 1 and 0 <= b <= n - 1:
        return False
    return True
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def flood(startR, startC):
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[startR][startC] = True
    stack = [(startR, startC)]
    cowSeen = 0
    while stack:
        uR, uC = stack.pop()
        for dR, dC in directions:
            vR, vC = uR + dR, uC + dC
            if out(vR, vC):
                continue
            if roads[(uR, uC, vR, vC)] or roads[(vR, vC, uR, uC)]:
                continue
            if not visited[vR][vC]:
                visited[vR][vC] = True
                stack.append((vR, vC))
                if (vR, vC) in locs:
                    cowSeen += 1
    return cowSeen

# see how many cows we can't access from each cow, then divide by 2 for repeat pairs
tot = 0
for loc in locs:
    seen = flood(loc[0], loc[1])
    tot += (k - 1) - seen
ans = tot // 2
print(ans)
