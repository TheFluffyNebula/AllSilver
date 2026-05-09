import sys
sys.stdin = open("lightson.in")
# sys.stdout = open("lightson.out", 'w')
from collections import defaultdict, deque

n, m = map(int, input().split())
switches = defaultdict(list)
for i in range(m):
    a, b, c, d = map(lambda x: int(x) - 1, input().split())
    switches[(a, b)].append((c, d))

allowed = [[False for _ in range(n)] for _ in range(n)]
allowed[0][0] = True
visited = [[False for _ in range(n)] for _ in range(n)]
visited[0][0] = True

q = deque([(0, 0)])
c = 1
while q:
    uX, uY = q.popleft()    
    for lightX, lightY in switches[(uX, uY)]:
        if not allowed[lightX][lightY]:
            print(lightX, lightY)
            allowed[lightX][lightY] = True
            c += 1
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        vX, vY = uX + dx, uY + dy
        if not (0 <= vX <= n - 1 and 0 <= vY <= n - 1):
            continue
        if not allowed[vX][vY]:
            continue
        if not visited[vX][vY]:
            visited[vX][vY] = True
            q.append((vX, vY))
            for lightX, lightY in switches[(vX, vY)]:
                if not allowed[lightX][lightY]:
                    print(lightX, lightY)
                    allowed[lightX][lightY] = True
                    c += 1
print(c)

'''
repeat flood until we don't light anything new
'''
