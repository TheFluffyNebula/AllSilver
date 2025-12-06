import sys
sys.stdin = open("vacation.in")
sys.stdout = open("vacation.out", 'w')
from collections import deque

n, m, k, q = map(int, input().split())
adj = {i: [] for i in range(n)}
for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append((w, b))

dist = [[float('inf') for _ in range(n)] for _ in range(n)]
def dijkstra(x):
    q = deque()
    q.append((0, x))
    dist[x][x] = 0
    while q:
        c, u = q.popleft()
        if c > dist[x][u]:
            continue
        for w, v in adj[u]:
            alt = dist[x][u] + w
            if alt < dist[x][v]:
                dist[x][v] = alt
                q.append((alt, v))
for i in range(n):
    dijkstra(i)
# print(*dist, sep='\n')

ansNum = 0
ansCost = 0
for _ in range(q):
    a, b = map(int, input().split())
    best = float('inf')
    for i in range(k):
        # go from a to the hub, then hub to b
        cost = dist[a - 1][i] + dist[i][b - 1]
        best = min(best, cost)
    if best != float('inf'):
        ansNum += 1
        ansCost += best
print(ansNum)
print(ansCost)

'''
dijkstra's for all pairwise distances
process each query by trying a -> hub -> b for each hub
'''
