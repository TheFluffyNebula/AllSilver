import sys
sys.stdin = open("hps.in")
sys.stdout = open("hps.out", 'w')

n, k = map(int, input().split())
gestures = [input().strip() for _ in range(n)]
# print(gestures)
for i in range(n):
    if gestures[i] == 'H':
        gestures[i] = 0
    elif gestures[i] == 'P':
        gestures[i] = 1
    else:
        gestures[i] = 2
# print(gestures)

# H0, P1, S2
dp = [[[0 for _ in range(3)] for _ in range(k + 1)] for _ in range(n)]
dp[0][0][gestures[0]] = 1
for i in range(1, n):
    for j in range(k + 1):
        # no swap
        for g in range(3):
            dp[i][j][g] = max(dp[i][j][g], dp[i - 1][j][g] + int(gestures[i] == g))
        if j > 0:
            # h -> p
            dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j - 1][0] + int(gestures[i] == 1))
            # h -> s
            dp[i][j][2] = max(dp[i][j][2], dp[i - 1][j - 1][0] + int(gestures[i] == 2))
            # p -> h
            dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j - 1][1] + int(gestures[i] == 0))
            # p -> s
            dp[i][j][2] = max(dp[i][j][2], dp[i - 1][j - 1][1] + int(gestures[i] == 2))
            # s -> h
            dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j - 1][2] + int(gestures[i] == 0))
            # s -> p
            dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j - 1][2] + int(gestures[i] == 1))
# print(dp)
ans = 0
for j in range(k + 1):
    for g in range(3):
        ans = max(ans, dp[-1][j][g])
print(ans)
'''
planning
dp(index, swaps, last gesture)
transitions: no swap, swap

swap to rolling dp if MLE
'''

'''
drafting
prefix sums for dp?
I don't see it at the moment, each state dp(index', switches') = maxWins
    can be reached from all states (all index <= index', switches' - 1)

another idea: try starting out as h/p/s, for each
    find the <= k most optimal switches

reminds me mathworks interview problem
choose k to take their option A over B, choose k best A - B values

if there were only two gestures, would that help
ex. want 0 vs. want 1 in other segments
start 0, swap to 1 in most optimal segments
    but choosing these segments... :(

OK, just regular dp, index-1 accounts for all paths
    I forgor haha
'''
