import sys
sys.stdin = open("gravity.in")
sys.stdout = open("gravity.out", 'w')
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
# print(*board, sep='\n')

q = deque()

dist = [[[float('inf') for _ in range(2)] for _ in range(m)] for _ in range(n)]
endX, endY = -1, -1
for i in range(n):
    for j in range(m):
        # make sure we're standing on a block
        if board[i][j] == "C":
            dist[i][j][0] = 0
            solidGround = False
            for k in range(i + 1, n):
                if board[k][j] == "#":
                    # we found solid ground
                    dist[k - 1][j][0] = 0
                    solidGround = True
                    # starting down
                    q.append((k - 1, j, False))
                    break
                else:
                    # falling through here
                    dist[k][j][0] = 0
            if not solidGround:
                print(-1)
                exit()
        elif board[i][j] == "D":
            endX, endY = i, j
# print(*dist, sep='\n')
# print(q)

def out(a, b):
    if a < 0 or a > n - 1 or b < 0 or b > m - 1:
        return True
    if board[a][b] == "#":
        return True
    return False

# storing up as a third state in addition to x & y
while q:
    # x and y are misnamed ._.
    curX, curY, up = q.popleft()
    for option in ("L", "R", "flip"):
        if option == "L" or option == "R":
            if option == "L":
                newY = curY - 1
            else:
                newY = curY + 1
            if out(curX, newY):
                continue
            alt = dist[curX][curY][up]
            # prune
            if alt >= dist[curX][newY][up]:
                continue
            # perform the operation
            if up:
                for i in range(curX, -1, -1):
                    if board[i][newY] == "#":
                        q.append((i + 1, newY, up))
                        break
                    dist[i][newY][up] = min(dist[i][newY][up], alt)
            else:
                for i in range(curX, n):
                    if board[i][newY] == "#":
                        q.append((i - 1, newY, up))
                        break
                    dist[i][newY][up] = min(dist[i][newY][up], alt)            
        else:
            # print("hi :(")
            newUp = not up
            alt = dist[curX][curY][up] + 1
            # prune
            if alt >= dist[curX][curY][newUp]:
                continue
            # perform the operation
            if newUp:
                for i in range(curX, -1, -1):
                    if board[i][curY] == "#":
                        q.append((i + 1, curY, newUp))
                        break
                    dist[i][curY][newUp] = min(dist[i][curY][newUp], alt)
            else:
                for i in range(curX, n):
                    if board[i][curY] == "#":
                        q.append((i - 1, curY, newUp))
                        break
                    dist[i][curY][newUp] = min(dist[i][curY][newUp], alt)   
# print(*dist, sep='\n')
ans = min(dist[endX][endY])
# print(ans)
print(-1) if ans == float('inf') else print(min(dist[endX][endY]))
