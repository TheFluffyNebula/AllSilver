# TLE, 12/15
import sys
sys.stdin = open("marathon.in")
sys.stdout = open("marathon.out", 'w')
from functools import lru_cache
sys.setrecursionlimit(3 * 10 ** 5)

n, k = map(int, input().split())
checkpoints = [tuple(map(int, input().split())) for _ in range(n)]

@lru_cache(None)
def dp(i, skips):
    if i >= n - 1:
        return 0
    ret = float('inf')
    # try all skip options
    for newSkips in range(1, k - skips + 1):
        newLoc = i + newSkips + 1
        if newLoc > n - 1:
            continue
        d = abs(checkpoints[newLoc][0] - checkpoints[i][0]) + abs(checkpoints[newLoc][1] - checkpoints[i][1])
        ret = min(ret, d + dp(newLoc, skips + newSkips))
    # take normal
    d = abs(checkpoints[i + 1][0] - checkpoints[i][0]) + abs(checkpoints[i + 1][1] - checkpoints[i][1])
    ret = min(ret, d + dp(i + 1, skips))
    return ret

ans = dp(0, 0)
print(ans)

'''
dp(i, skips) = min distance at checkpoint i using [skips] skips
'''
