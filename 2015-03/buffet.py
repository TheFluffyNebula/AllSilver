import sys
sys.stdin = open("buffet.in")
sys.stdout = open("buffet.out", 'w')
input = sys.stdin.readline
from collections import deque
from functools import lru_cache
sys.setrecursionlimit(10 ** 5)

'''
what if we create a distances table via bfs from every node
now, dist[source][dest] is O(1)
from there, start at each one and go to others
sounds like a O(n^2) DP
'''

n, e = map(int, input().split())
adj = {i: [] for i in range(n)}
quality = [0] * n
edges = set()
for a in range(n):
    nums = list(map(int, input().split()))
    q = nums[0]
    quality[a] = q
    connections = nums[1]
    for j in range(connections):
        idx = 2 + j
        b = nums[idx] - 1
        if (min(a, b), max(a, b)) not in edges:
            adj[a].append(b)
            adj[b].append(a)
            edges.add((min(a, b), max(a, b)))
# print(adj)

def bfs(start):
    q = deque()
    dist[start][start] = 0
    q.append((start, 0))
    while q:
        u, uCost = q.popleft()
        for v in adj[u]:
            alt = uCost + 1
            if alt < dist[start][v]:
                dist[start][v] = alt
                q.append((v, alt))

dist = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(n):
    bfs(i)
# print(dist)

# define the order of which we can traverse
# (quality, index)
qualities = list(zip(quality, [i for i in range(n)]))
qualities.sort()
# print(qualities)

@lru_cache(None)
def dp(i):
    if i == n - 1:
        return 0
    ret = 0
    for j in range(i + 1, n):
        if qualities[i][0] == qualities[j][0]:
            continue
        ret = max(ret, dp(j) + qualities[j][0] - e * dist[qualities[i][1]][qualities[j][1]])
    return ret

ans = 0
# start from each spot, go in reverse to use the cache better?
for i in range(n - 1, -1, -1):
    ans = max(ans, qualities[i][0] + dp(i))
    dp.cache_clear()
print(ans)
