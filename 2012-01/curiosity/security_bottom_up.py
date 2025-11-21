a = [5, 6, 7, 2]
s = "0111"

n = len(s)
dp = [[0] * 2 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(2):
        if s[i - 1] == "1" and j == 0:
            dp[i][j] = max(dp[i][j], a[i - 1] + dp[i - 1][0])
        else:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if i < n:
                if s[i] == "1":
                    dp[i][1] = max(dp[i][j], a[i - 1] + dp[i - 1][1])
print(dp)

print(max(dp[n]))

'''
def dp(i, gotYoinked):
    # print(i, gotYoinked)z
    if i == n:
        return 0
    ret = 0
    if s[i] == "1" and not gotYoinked:
        # already secured, go next
        ret = max(ret, a[i] + dp(i + 1, False))
    else:
        # not secured, can either stay or yoink from next
        # stay
        ret = max(ret, dp(i + 1, False))
        # yoink from next (if next has a 1)
        if i < n - 1:
            if s[i + 1] == "1":
                ret = max(ret, a[i] + dp(i + 1, True))
    return ret

PS: 
1. not 100% sure the bottom-up version is correct but the printed numbers look right
2. for the top-down version, you can print (i, gotYoinked) while toggling @cache to see reduces function calls to at most 2 * n
'''

