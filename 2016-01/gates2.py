# surefire way to work
# oop, TLE
import sys
sys.stdin = open("gates.in")
sys.stdout = open("gates.out", 'w')
input = sys.stdin.readline

n = int(input())
s = input().strip()

directionMap = {
    "N": (0, 2), 
    "S": (0, -2), 
    "E": (2, 0), 
    "W": (-2, 0)
}

board = [[0 for _ in range(2000)] for _ in range(2000)]
curX, curY = 0, 0
for i in range(n):
    prevX, prevY = curX, curY
    curX += directionMap[s[i]][0]
    curY += directionMap[s[i]][1]
    betweenX, betweenY = (prevX + curX) // 2, (prevY + curY) // 2
    board[prevX][prevY] = 1
    board[betweenX][betweenY] = 1
    board[curX][curY] = 1

def flood(i, j):
    stack = [(i, j)]
    visited[i][j] = True
    while stack:
        uX, uY = stack.pop()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            vX, vY = uX + dx, uY + dy
            if not (-2000 <= vX <= 1999 and -2000 <= vY <= 1999):
                continue
            if board[vX][vY]:
                continue
            if not visited[vX][vY]:
                stack.append((vX, vY))
                visited[vX][vY] = True

visited = [[False for _ in range(2000)] for _ in range(2000)]
components = 0
for i in range(2000):
    for j in range(2000):
        if board[i][j]:
            continue
        if not visited[i][j]:
            components += 1
            flood(i, j)
print(components - 1)

'''
abusing Python negative indexing
'''