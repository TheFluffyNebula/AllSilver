import sys
# sys.stdin = open("tractor.in")
input = sys.stdin.readline
from collections import deque

n, startX, startY = map(int, input().split())
bales = [[False for _ in range(1002)] for _ in range(1002)]
for i in range(n):
    a, b = map(int, input().split())
    bales[a][b] = True

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def out(a, b):
    if a < 0 or a > 1001 or b < 0 or b > 1001:
        return True
    return False

dist = [[float('inf') for _ in range(1002)] for _ in range(1002)]
dist[startX][startY] = 0
q = deque()
q.append((startX, startY))
while q:
    cx, cy = q.popleft()
    for dx, dy in DIRECTIONS:
        x = cx + dx
        y = cy + dy
        if out(x, y):
            continue
        alt = dist[cx][cy]
        cost = bales[x][y]
        if alt + cost < dist[x][y]:
            dist[x][y] = alt + cost
            if cost:
                q.append((x, y))
            else:
                q.appendleft((x, y))

print(dist[0][0])

'''
dijkstra's from tractor to (0, 0)
no-bale = same distance, bale = +1
most critical error: not allowing FJ to travel outside where the bales could be (1-1000)
alternatively, 0-1 bfs (0 = appendleft, 1 = append)
'''
