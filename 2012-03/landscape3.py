# solution peek: dp
import sys
# sys.stdin = open("landscape.in")
input = sys.stdin.readline

spots, x, y, z = map(int, input().split())
s1 = []
s2 = []
for i in range(spots):
    a, b = map(int, input().split())
    s1.extend([i] * a)
    s2.extend([i] * b)
# print(s1, s2)

n = len(s1)
m = len(s2)
dp = [[float('inf') for _ in range(m)] for _ in range(n)]
for i in range(n):
    dp[i][0] = i * y
for j in range(m):
    dp[0][j] = j * x

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = min(dp[i][j], dp[i][j - 1] + x)
        dp[i][j] = min(dp[i][j], dp[i - 1][j] + y)
        dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + z * abs(s1[i] - s2[j]))

ans = dp[n - 1][m - 1]
print(ans)

'''
insert: x
delete: y
modify: z * magnitude-of-change

"Each subproblem C[i][j] we solve along the way represents the minimum cost of transforming just 
the first i characters of the source sequence into just the first j characters of the target sequence."
'''
