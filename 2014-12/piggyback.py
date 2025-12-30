import sys
sys.stdin = open("piggyback.in")
sys.stdout = open("piggyback.out", 'w')
from collections import deque

b, e, p, n, m = map(int, input().split())

adj = {i: [] for i in range(n)}
for i in range(m):
    node1, node2 = map(int, input().split())
    node1 -= 1
    node2 -= 1
    adj[node1].append(node2)
    adj[node2].append(node1)

bDist = [float('inf')] * n
# bDist[0] = 0
eDist = [float('inf')] * n
# eDist[1] = 0
pDist = [float('inf')] * n
# pDist[n - 1] = 0

def bfs(dist, start):
    dist[start] = 0
    visited = [False] * n
    visited[start] = True
    q = deque()
    q.append((start, 0))
    while q:
        u, c = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = c + 1
                q.append((v, c + 1))

bfs(bDist, 0)
bfs(eDist, 1)
bfs(pDist, n - 1)
# print(bDist, eDist, pDist)

ans = float('inf')
# i = n - 1 is the no piggyback scenario
for i in range(n):
    bTravel = bDist[i] * b
    eTravel = eDist[i] * e
    pTravel = pDist[i] * p
    # print(i, bTravel, eTravel, pTravel)
    ans = min(ans, bTravel + eTravel + pTravel)
print(ans)

'''
two scenarios: piggyback or no piggyback (take min)

no piggyback --> dijkstra's for both, add

piggyback: when p < (b + e)
oh! compute all piggyback -> end (dijkstra from end)
store these values.
then, dijkstra from 1 to all & 2 to all
finally, iterate through all 1+2+piggyback values on each node
'''
