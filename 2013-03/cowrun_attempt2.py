# copied from solution notes
import sys
sys.stdin = open("cowrun.in")
sys.stdout = open("cowrun.out", 'w')
input = sys.stdin.readline

n = int(input())
cows = [int(input()) for _ in range(n)]
cows.append(0)
n += 1
cows.sort()

start_pos = cows.index(0)

dp = [[[float('inf')] * 2 for _ in range(n + 1)] for _ in range(n + 1)]

dp[start_pos][1][0] = 0
dp[start_pos][1][1] = 0

for length in range(1, n):
    remaining = n - length
    for i in range(n - length + 1):
        # Extend to the left
        if i > 0:
            dp[i - 1][length + 1][0] = min(
                dp[i - 1][length + 1][0],
                # from left going left
                dp[i][length][0] + remaining * (cows[i] - cows[i - 1]),
                # from right going left
                dp[i][length][1] + remaining * (cows[i + length - 1] - cows[i - 1])
            )
        
        # Extend to the right
        if i + length < n:
            dp[i][length + 1][1] = min(
                dp[i][length + 1][1],
                # from left going right
                dp[i][length][0] + remaining * (cows[i + length] - cows[i]),
                # from right going right
                dp[i][length][1] + remaining * (cows[i + length] - cows[i + length - 1])
            )

print(min(dp[0][n][0], dp[0][n][1]))

# from functools import cache
# zeroIdx = cows.index(0)
# print(zeroIdx)
# @cache
# def dp(L, R, left):
#     if L == 0 and R == n - 1:
#         return 0
#     ret = float('inf')
#     # the key variable I missed -- how to count earlier entries multiple times
#     ccount = n - (R - L)
#     # go left
#     if L > 0:
#         if left:
#             ret = min(ret, ccount * (cows[L] - cows[L - 1]) + dp(L - 1, R, 1))
#         else:
#             ret = min(ret, ccount * (cows[R] - cows[L - 1]) + dp(L - 1, R, 0))
#     # go right
#     if R < n - 1:
#         if not left:
#             ret = min(ret, ccount * (cows[R + 1] - cows[R]) + dp(L, R + 1, 1))
#         else:
#             ret = min(ret, ccount * (cows[R + 1] - cows[L]) + dp(L, R + 1, 0))
#     return ret

# ans = dp(zeroIdx, zeroIdx, 0)
# print(ans)
