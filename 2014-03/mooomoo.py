import sys
sys.stdin = open("mooomoo.in")
sys.stdout = open("mooomoo.out", 'w')

n, b = map(int, input().split())
cows = [int(input()) for _ in range(b)]
# pad so we pick up the first volume
volumes = [0] + [int(input()) for _ in range(n)]
# print(cows, volumes)

diffs = []

for i in range(n):
    diff = volumes[i] - volumes[i + 1]
    if diff == 0:
        # 0 to 0
        if volumes[i] == 0:
            continue
        # cow of volume 1 here instead (covered below)
    # volume decreases by one naturally, no cow here
    if diff == 1:
        continue
    # impossible case, sound dropping off by more than 1
    if diff > 1:
        print(-1)
        exit()
    diffs.append(volumes[i + 1] - max(0, volumes[i] - 1))
# print(diffs)

if len(diffs) == 0:
    print(0)
    exit()

diffs.sort()
mx = diffs[-1]
dp = [float('inf')] * (mx + 1)
dp[0] = 0
# iterate forward since there can be multiple of a cow
cows.sort()
for v in cows:
    dp[v] = 1
    for j in range(v + 1, mx + 1):
        dp[j] = min(dp[j], dp[j - v] + 1)

# print(dp)
ans = 0
for d in diffs:
    ans += dp[d]
print(ans) if ans != float('inf') else print(-1)

'''
oh! I understand it now
0/1 knapsack
'''
