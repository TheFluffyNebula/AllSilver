# TLE 8/10, will try union-find later
import sys
sys.stdin = open("tractor.in")
sys.stdout = open("tractor.out", 'w')
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
# print(*board, sep='\n')
adj = defaultdict(list)
for i in range(n):
    for j in range(n):
        if i > 0:
            node = ((i - 1, j), abs(board[i][j] - board[i - 1][j]))
            adj[(i, j)].append(node)
        if i < n - 1:
            node = ((i + 1, j), abs(board[i][j] - board[i + 1][j]))
            adj[(i, j)].append(node)
        if j > 0:
            node = ((i, j - 1), abs(board[i][j] - board[i][j - 1]))
            adj[(i, j)].append(node)
        if j < n - 1:
            node = ((i, j + 1), abs(board[i][j] - board[i][j + 1]))
            adj[(i, j)].append(node)
# print(adj)

def dfs(startX, startY, d):
    c = 1
    stack = [(startX, startY)]
    visited[startX][startY] = True
    while stack:
        curX, curY = stack.pop()
        for v, w in adj[(curX, curY)]:
            if d < w:
                continue
            if not visited[v[0]][v[1]]:
                c += 1
                stack.append(v)
                visited[v[0]][v[1]] = True
    return c

def good(d):
    global visited
    visited = [[False for _ in range(n)] for _ in range(n)]  
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                componentSize = dfs(i, j, d)                
                if componentSize >= half:
                    return True
    return False

half = n ** 2 // 2
if n % 2 == 1:
    half += 1  

L = 0
R = 10 ** 6
ans = -1
while L <= R:
    mid = (L + R) // 2
    if good(mid):
        ans = mid
        R = mid - 1
    else:
        L = mid + 1
print(ans)

'''
binary search on cost
floodfill to find largest component
'''
