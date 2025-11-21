import sys
sys.stdin = open("bbreeds.in")
sys.stdout = open("bbreeds.out", 'w')
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
import functools

s = input().strip()
n = len(s)
@functools.lru_cache(maxsize=None)
def dp(i, G, H):
    if i == n:
        if G == 0 and H == 0:
            return 1
        return 0
    ret = 0
    if s[i] == '(':
        ret += dp(i + 1, G + 1, H)
        ret += dp(i + 1, G, H + 1)
    else:
        if G == 0 and H == 0:
            return 0
        if G > 0:
            ret += dp(i + 1, G - 1, H)
        if H > 0:
            ret += dp(i + 1, G, H - 1)
    return ret
ans = dp(0, 0, 0)
print(ans % 2012)
'''
dp idea:
O(n^3) method: i, G, H
index, G-left, H-left
wait... it worked!!
'''
