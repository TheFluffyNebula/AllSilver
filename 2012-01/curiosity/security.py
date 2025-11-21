a = [5, 6, 7, 2]
s = "0111"

from functools import cache

n = len(a)
@cache
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

ans = dp(0, False)
print(ans)
