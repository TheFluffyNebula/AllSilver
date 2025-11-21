import sys
sys.stdin = open("wifi.in")
sys.stdout = open("wifi.out", 'w')
input = sys.stdin.readline

n, a, b = map(int, input().split())
cows = [int(input()) for _ in range(n)]
cows.sort()
# print(cows)

# dp[i + 1] represents min cost for providing connection for the first i cows
dp = [float('inf') for _ in range(n + 1)]
dp[0] = 0
# give connection cows in the range of [i, j]
for i in range(n):
    for j in range(i, n):
        minCow = cows[i]
        maxCow = cows[j]
        power = (maxCow - minCow) / 2
        cost = a + b * power
        dp[j + 1] = min(dp[j + 1], dp[i] + cost)
        # if i == 0 and j == 2:
        #     print(dp)
# print(dp)
if dp[n] == int(dp[n]):
    print(int(dp[n]))
else:
    print(dp[n])
