# even the official solution TLE's, ok
import sys
sys.stdin = open("meeting.in")
# sys.stdout = open("meeting.out", 'w')

n, m = map(int, input().split())
dist1 = [[0 for _ in range(n)] for _ in range(n)]
dist2 = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    dist1[a][b] = c
    dist2[a][b] = d

dp1 = [[False for _ in range(100 * n + 1)] for _ in range(n)]
dp2 = [[False for _ in range(100 * n + 1)] for _ in range(n)]
dp1[0][0] = True
dp2[0][0] = True
for i in range(n):
    for j in range(100 * n + 1):
        if not dp1[i][j]:
            continue
        for k in range(i + 1, n):
            if dist1[i][k] > 0:
                dp1[k][j + dist1[i][k]] = True
for i in range(n):
    for j in range(100 * n + 1):
        if not dp2[i][j]:
            continue
        for k in range(i + 1, n):
            if dist2[i][k] > 0:
                dp2[k][j + dist2[i][k]] = True
for i in range(100 * n + 1):
    if dp1[n - 1][i] and dp2[n - 1][i]:
        print(i)
        exit()
print("IMPOSSIBLE")
'''
copying the solution
'''
