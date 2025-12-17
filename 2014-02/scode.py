import sys
sys.stdin = open("scode.in")
sys.stdout = open("scode.out", 'w')
from functools import lru_cache

s = input().strip()

@lru_cache(None)
def dp(s):
    # print(s)
    if len(s) == 1 or len(s) == 2:
        # print(s)
        return 0

    ret = 0
    n = len(s)
    for i in range(1, n):
        # four things to try for each split:
        # prefix + s, suffix + s, s + prefix, s + suffix
        pf = s[:i]
        sf = s[i:]
        # print(pf, sf)
        pf_len = len(pf)
        sf_len = len(sf)
        if pf_len < sf_len:
            # s = sf
            if pf == sf[:i]:
                ret += 1 + dp(sf)
            if pf == sf[-pf_len:]:
                ret += 1 + dp(sf)
        if sf_len < pf_len:
            # s = pf
            if sf == pf[:sf_len]:
                ret += 1 + dp(pf)
            if sf == pf[-sf_len:]:
                ret += 1 + dp(pf)
    ret %= 2014
    return ret

ans = dp(s)
print(ans)
