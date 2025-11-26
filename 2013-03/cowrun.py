import sys
sys.stdin = open("cowrun.in")
input = sys.stdin.readline
from functools import cache

n = int(input())
cows = [int(input()) for _ in range(n)]
cows.sort()
# print(cows)
pos = []
neg = []
for i in range(n):
    if cows[i] > 0:
        pos.append(cows[i])
    else:
        neg.append(cows[i])
neg = neg[::-1]
# print(pos, neg)

pf_pos = [0]
pf_neg = [0]
for i in range(len(pos)):
    pf_pos.append(pf_pos[-1] + pos[i])
for i in range(len(neg)):
    pf_neg.append(pf_neg[-1] + abs(neg[i]))

@cache
def dp(i, L, inPositiveList):
    if i == n:
        return 0
    ret = float('inf')
    negIdx = L
    posIdx = i - L
    time = pf_pos[posIdx - 1] + pf_neg[negIdx - 1]
    if inPositiveList:
        # stay in the positive list
        if posIdx < len(pos):
            distance = pos[posIdx] - pos[posIdx - 1]
            ret = min(ret, time + distance + dp(i + 1, L, 1))
        # go to the negative list
        if negIdx < len(neg):
            distance = pos[posIdx - 1] + abs(neg[negIdx])
            ret = min(ret, time + distance + dp(i + 1, L + 1, 0))
    else:
        # stay in the negative list
        if negIdx < len(neg):
            distance = abs(neg[negIdx] - neg[negIdx - 1])
            ret = min(ret, time + distance + dp(i + 1, L + 1, 0))
        # go to the positive list
        if posIdx < len(pos):
            distance = abs(neg[negIdx - 1]) + pos[posIdx]
            ret = min(ret, time + distance + dp(i + 1, L, 1))
    return ret
# 0 for no, 1 for yes (just took a positive number)
# maximum states: 1000 * 1000 * 2
ans = min(abs(neg[0]) + dp(1, 1, 0), pos[0] + dp(1, 0, 1))
print(ans)

'''
on first glance, greedy approach?
always go to the closest one
well, perhaps not ex. lots of negatives, one single close positive
previous decisions influence next ones, can get to same state via multiple routes --> dp?

dp idea: (i, L) on the ith cow, how many L selections we've taken
R state gets compressed to i - L

oof, didn't implement it cleanly
solution notes: track interval of cows visited (L, R)
'''
