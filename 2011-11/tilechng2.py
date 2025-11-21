import sys
# sys.stdin = open("tilechng.in")
input = sys.stdin.readline

n, m = map(int, input().split())
tiles = [int(input()) for _ in range(n)]

dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
# zero tiles, zero area
dp[0][0] = 0
# dp[i][j] = minn cost at i tiles, j area
# print(dp)

for i in range(1, n + 1):
    for j in range(m + 1):
        for tile_size in range(1, 101):
            prev = j - tile_size ** 2
            # no point in testing any larger tiles
            if prev < 0:
                break
            # compare to current tile size
            cost = abs(tile_size - tiles[i - 1]) ** 2
            dp[i][j] = min(dp[i][j], dp[i - 1][prev] + cost)
print(dp[n][m]) if dp[n][m] != float('inf') else print(-1)

'''
peeked the solution, DP (appears to be knapsack)
'''
