# TLE, 7/15 (exponential dfs)
import sys
sys.stdin = open("meeting.in")
# sys.stdout = open("meeting.out", 'w')
from functools import lru_cache

n, m = map(int, input().split())
adj1 = {i: [] for i in range(n)}
adj2 = {i: [] for i in range(n)}
for i in range(m):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    adj1[a].append((b, c))
    adj2[a].append((b, d))
# print(adj1, adj2)

times1 = set()
times2 = set()
@lru_cache(None)
def search(u, t):
    if u == n - 1:
        times1.add(t)
        return
    for v, w in adj1[u]:
        search(v, t + w)
    return
@lru_cache(None)
def search2(u, t):
    if u == n - 1:
        times2.add(t)
        return
    for v, w in adj2[u]:
        search2(v, t + w)
    return
search(0, 0)
search2(0, 0)
# print(times1, times2)
commonTimes = times1.intersection(times2)
if commonTimes:
    print(min(commonTimes))
else:
    print("IMPOSSIBLE")
