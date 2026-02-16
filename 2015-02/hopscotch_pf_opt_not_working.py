# fully gpt'd, DOES NOT WORK, just here for reference/curiosity later
import sys
sys.stdin = open("hopscotch.in")
sys.stdout = open("hopscotch.out", 'w')
input = sys.stdin.readline

MOD = 10 ** 9 + 7

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

dp = [[0]*c for _ in range(r)]
dp[0][0] = 1

# column prefix sums
colPref = [[0]*c for _ in range(r)]

# color-specific column prefix sums
from collections import defaultdict
colorColPref = defaultdict(lambda: [[0]*c for _ in range(r)])

for i in range(r):
    for j in range(c):

        if i == 0 and j == 0:
            colPref[0][0] = 1
            colorColPref[board[0][0]][0][0] = 1
            continue

        total = 0
        same = 0

        # sum over y < j
        for y in range(j):
            if i > 0:
                total += colPref[i-1][y]
                same += colorColPref[board[i][j]][i-1][y]

        dp[i][j] = (total - same) % MOD

        # update column prefix sums
        if i == 0:
            colPref[i][j] = dp[i][j]
            colorColPref[board[i][j]][i][j] = dp[i][j]
        else:
            colPref[i][j] = (colPref[i-1][j] + dp[i][j]) % MOD
            colorColPref[board[i][j]][i][j] = (
                colorColPref[board[i][j]][i-1][j] + dp[i][j]
            ) % MOD

print(dp[r-1][c-1])
