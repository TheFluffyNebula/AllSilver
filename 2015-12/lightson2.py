# let's clean it up
import sys
sys.stdin = open("lightson.in")
sys.stdout = open("lightson.out", 'w')
from collections import defaultdict

n, m = map(int, input().split())
adj = defaultdict(list)
for i in range(m):
    a, b, c, d = map(lambda x: int(x) - 1, input().split())
    adj[(a, b)].append((c, d))
# print(adj)

def out(a, b):
    if a < 0 or a > n - 1 or b < 0 or b > n - 1:
        return True
    return False

def flood():
    global tot
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    ret = False
    stack = [(0, 0)]
    for newLitX, newLitY in adj[(0, 0)]:
        if not lit[newLitX][newLitY]:
            ret = True
            lit[newLitX][newLitY] = True
            tot += 1
    while stack:
        uX, uY = stack.pop()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            vX, vY = uX + dx, uY + dy
            if out(vX, vY) or visited[vX][vY] or not lit[vX][vY]:
                continue
            visited[vX][vY] = True
            stack.append((vX, vY))
            for newLitX, newLitY in adj[(vX, vY)]:
                if not lit[newLitX][newLitY]:
                    ret = True
                    lit[newLitX][newLitY] = True
                    tot += 1
    return ret
tot = 1
new = True
lit = [[False for _ in range(n)] for _ in range(n)]
lit[0][0] = True
while new:
    new = flood()
# print(lit)
print(tot)

'''
I'll try inverting the order.
1. flood to lit rooms
2. new lights? turn stuff on, repeat 1
   else? break
'''
