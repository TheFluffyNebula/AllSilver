# still TLE and wrong -- I guess my solution is nk^2
import sys
sys.stdin = open("marathon.in")
# sys.stdout = open("marathon.out", 'w')

n, k = map(int, input().split())
checkpoints = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[float('inf') for _ in range(k + 1)] for _ in range(n)]
dp[0][0] = 0
for i in range(n - 1):
    for j in range(k):
        # from (0, 0) where can we go?
        for newSkips in range(1, k - j + 1):
            newLoc = i + newSkips + 1
            if newLoc > n - 1 or j + newSkips > k:
                continue
            d = abs(checkpoints[newLoc][0] - checkpoints[i][0]) + abs(checkpoints[newLoc][1] - checkpoints[i][1])
            dp[newLoc][j + newSkips] = min(dp[newLoc][j + newSkips], d + dp[i][j])
        d = abs(checkpoints[i + 1][0] - checkpoints[i][0]) + abs(checkpoints[i + 1][1] - checkpoints[i][1])
        dp[i + 1][j] = min(dp[i + 1][j], d + dp[i][j])

# print(dp)
print(min(dp[-1]))

# @lru_cache(None)
# def dp(i, skips):
#     if i >= n - 1:
#         return 0
#     ret = float('inf')
#     # try all skip options
#     for newSkips in range(1, k - skips + 1):
#         newLoc = i + newSkips + 1
#         if newLoc > n - 1:
#             continue
#         d = abs(checkpoints[newLoc][0] - checkpoints[i][0]) + abs(checkpoints[newLoc][1] - checkpoints[i][1])
#         ret = min(ret, d + dp(newLoc, skips + newSkips))
#     # take normal
#     d = abs(checkpoints[i + 1][0] - checkpoints[i][0]) + abs(checkpoints[i + 1][1] - checkpoints[i][1])
#     ret = min(ret, d + dp(i + 1, skips))
#     return ret
