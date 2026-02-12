import sys
sys.stdin = open("hopscotch.in")
# sys.stdout = open("hopscotch.out", 'w')
input = sys.stdin.readline

MOD = 10 ** 9 + 7

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
# print(*board, sep='\n')

# jump from every square to the current one being processed
# TC: R**2 * C**2
# ok, there's probably a way to speed this up
dp = [[0 for _ in range(c)] for _ in range(r)]
dp[0][0] = 1
for i in range(1, r):
    for j in range(1, c):
        for x in range(i):
            for y in range(j):
                if board[i][j] != board[x][y]:
                    dp[i][j] += dp[x][y]
        dp[i][j] %= MOD
print(dp[-1][-1])
