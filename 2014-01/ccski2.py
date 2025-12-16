# ok, let's try dijkstra!
# TLE 9/10
import sys
sys.stdin = open("ccski.in")
sys.stdout = open("ccski.out", 'w')
# from queue import PriorityQueue
import heapq

m, n = map(int, input().split())
course = [list(map(int, input().split())) for _ in range(m)]
waypoints = [list(map(int, input().split())) for _ in range(m)]
# print(*course, sep='\n')
# print(*waypoints, sep='\n')
startRow, startCol = -1, -1
for i in range(m):
    for j in range(n):
        if waypoints[i][j]:
            startRow = i
            startCol = j
            break

pq = []
heapq.heapify(pq)
heapq.heappush(pq, (0, startRow, startCol))
best = [[float('inf') for _ in range(n)] for _ in range(m)]
best[startRow][startCol] = 0
while len(pq):
    cost, curX, curY = heapq.heappop(pq)
    if cost > best[curX][curY]:
        continue
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        x = curX + dx
        y = curY + dy
        # in bounds?
        if 0 <= x <= m - 1 and 0 <= y <= n - 1:
            newCost = max(cost, abs(course[curX][curY] - course[x][y]))
            if newCost < best[x][y]:
                heapq.heappush(pq, (newCost, x, y))
                best[x][y] = newCost
ans = 0
for i in range(m):
    for j in range(n):
        if waypoints[i][j]:
            ans = max(ans, best[i][j])
print(ans)
'''
one pass, dijkstra
'''
