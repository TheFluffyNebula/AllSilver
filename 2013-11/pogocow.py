# WA and TLE :(
import sys
sys.stdin = open("pogocow.in")
# sys.stdout = open("pogocow.out", 'w')
from functools import lru_cache

n = int(input())
targets = [list(map(int, input().split())) for _ in range(n)]
targets.sort()
# print(targets)
loc, pts = map(list, zip(*targets))
# print(loc)
# print(pts)

@lru_cache(maxsize=None)
def dp(i, prevIdx):
    ret = float('-inf')
    minNextTargetLoc = loc[i] + (loc[i] - loc[prevIdx]) + 1
    L = i
    R = n - 1
    nextIdx = -1
    while L <= R:
        mid = (L + R) // 2
        if loc[mid] >= minNextTargetLoc:
            nextIdx = mid
            R = mid - 1
        else:
            L = mid + 1
    if nextIdx == -1:
        return 0
    # print(nextIdx)
    for j in range(nextIdx, n):
        ret = max(ret, pts[j] + dp(j, i))
    return ret
ans = max(pts[i] + dp(i, i) for i in range(n))
# print(ans)

dp.cache_clear()
targets2 = [(-x, p) for (x, p) in targets]
targets2.sort()
loc, pts = map(list, zip(*targets2))
ans2 = max(pts[i] + dp(i, i) for i in range(n))
print(max(ans, ans2))

'''
interesting!
sort the input by locations
dp on going to each location?
dp(i, prevSpeed)
^^ when top-down is needed, replace w/ prevIdx?

tricky, peek + copy here
unless... I missed the right-to-left element (hence the WAs)
oof, too buggy
'''
