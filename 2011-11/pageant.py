import sys
# sys.stdin = open("pageant.in")
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
s = [input().strip() for _ in range(n)]

visited = [[False] * m for _ in range(n)]
board = [[0] * m for _ in range(n)]
# print(board)
spots = [[] for _ in range(3)]

def floodfill(startX, startY, num):
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def out(a, b):
        if a < 0 or a > n - 1 or b < 0 or b > m - 1:
            return True
        return False

    q = deque()
    q.append((startX, startY))
    visited[startX][startY] = True
    board[startX][startY] = num
    spots[num - 1].append((startX, startY))
    while q:
        curX, curY = q.popleft()
        # visited[curX][curY] = True
        # board[curX][curY] = num
        # spots[num - 1].append((curX, curY))
        for dx, dy in d:
            nX, nY = curX + dx, curY + dy
            if out(nX, nY) or visited[nX][nY]:
                continue
            if s[nX][nY] == 'X':
                q.append((nX, nY))
                visited[nX][nY] = True
                board[nX][nY] = num
                spots[num - 1].append((nX, nY))

num = 1
for i in range(n):
    for j in range(m):
        if s[i][j] == 'X' and not visited[i][j]:
            floodfill(i, j, num)
            num += 1
# print(num)
# print(*board, sep = '\n')
# print(spots)

'''
min((1-2 + 2-3 + 1-3), min(all midpoints to all 3))
'''

def checkPair(x, y):
    len1 = len(spots[x])
    len2 = len(spots[y])
    dist = float('inf')
    for i in range(len1):
        for j in range(len2):
            x1, y1 = spots[x][i]
            x2, y2 = spots[y][j]
            dist = min(dist, abs(x1 - x2) + abs(y1 - y2))
    # need one less connection than Manhattan distance
    # print(dist)
    return dist - 1

pair1 = checkPair(0, 1)
pair2 = checkPair(0, 2)
pair3 = checkPair(1, 2)
candidate1 = min((pair1 + pair2), (pair1 + pair3), (pair2 + pair3))
# print(candidate1)

def checkPoint(x, y):
    ret = 0
    for i in range(3):
        best = float('inf')
        spotLen = len(spots[i])
        for j in range(spotLen):
            best = min(best, (abs(spots[i][j][0] - x) + abs(spots[i][j][1] - y)) - 1)
        ret += best
    return ret + 1

candidate2 = float('inf')
for i in range(n):
    for j in range(m):
        if board[i][j] != 'X':
            candidate2 = min(candidate2, checkPoint(i, j))
# print(candidate2)
print(min(candidate1, candidate2))
