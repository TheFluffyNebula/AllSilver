# TLE, 5/10 testcases
import sys
sys.stdin = open("ccski.in")
sys.stdout = open("ccski.out", 'w')
from collections import deque

m, n = map(int, input().split())
course = [list(map(int, input().split())) for _ in range(m)]
waypoints = [list(map(int, input().split())) for _ in range(m)]
# print(*course, sep='\n')
# print(*waypoints, sep='\n')
startRow, startCol = -1, -1
numWaypoints = 0
for i in range(m):
    for j in range(n):
        if waypoints[i][j]:
            startRow = i
            startCol = j
            numWaypoints += 1
assert numWaypoints > 0

def check(mxDiff):
    c = 1
    q = deque([(startRow, startCol)])
    visited = [[False for _ in range(n)] for _ in range(m)]
    visited[startRow][startCol] = True
    while q:
        curX, curY = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x = curX + dx
            y = curY + dy
            if 0 <= x <= m - 1 and 0 <= y <= n - 1:
                # can we reach this block?
                if abs(course[curX][curY] - course[x][y]) > mxDiff:                    
                    continue
                if not visited[x][y]:
                    visited[x][y] = True
                    c += waypoints[x][y]
                    q.append((x, y))
    return c == numWaypoints

L = 0
R = 10 ** 9
ans = -1
while L <= R:
    mid = (L + R) // 2
    if check(mid):
        ans = mid
        R = mid - 1
    else:
        L = mid + 1
print(ans)

'''
binary search seems the simplest
w/ dijkstra as backup
'''
