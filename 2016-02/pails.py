import sys
sys.stdin = open("pails.in")
sys.stdout = open("pails.out", 'w')
from collections import deque

x, y, k, m = map(int, input().split())
dist = [[float('inf') for _ in range(y + 1)] for _ in range(x + 1)]
dist[0][0] = 0
q = deque()
# t, x, y
q.append((0, 0, 0))
while q:
    t, curX, curY = q.popleft()
    # operations: fillX, fillY, emptyX, emptyY, X -> Y, Y -> X
    if t > dist[curX][curY]:
        continue
    alt = t + 1
    if alt > k:
        continue
    # fill
    if alt < dist[x][curY]:
        dist[x][curY] = alt
        q.append((alt, x, curY))
    if alt < dist[curX][y]:
        dist[curX][y] = alt
        q.append((alt, curX, y))
    # empty
    if alt < dist[0][curY]:
        dist[0][curY] = alt
        q.append((alt, 0, curY))
    if alt < dist[curX][0]:
        dist[curX][0] = alt
        q.append((alt, curX, 0))
    # transfer X -> Y
    newX = min(x, curX + curY)
    transferred = newX - curX
    newY = curY - transferred
    if alt < dist[newX][newY]:
        dist[newX][newY] = alt
        q.append((alt, newX, newY))
        newX = min(x, curX + curY)
    # transfer Y -> X
    newY = min(y, curX + curY)
    transferred = newY - curY
    newX = curX - transferred
    if alt < dist[newX][newY]:
        dist[newX][newY] = alt
        q.append((alt, newX, newY))

best = float('inf')
for i in range(x + 1):
    for j in range(y + 1):
        if dist[i][j] < float('inf'):
            best = min(best, abs(m - (i + j)))
print(best)
'''
bfs/djijkstra's, look for the closest
should be p efficient due to constraint on m
at most 40,000 states to traverse through
'''
