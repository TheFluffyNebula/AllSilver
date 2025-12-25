import sys
sys.stdin = open("gpsduel.in")
sys.stdout = open("gpsduel.out", 'w')
from collections import defaultdict
import heapq

n, m = map(int, input().split())
adj1 = {i: [] for i in range(n)}
adj2 = {i: [] for i in range(n)}
adj_simple = {i: [] for i in range(n)}
for i in range(m):
    a, b, p, q = map(int, input().split())
    a -= 1
    b -= 1
    adj1[b].append((a, p))
    adj2[b].append((a, q))
    adj_simple[a].append(b)

# mark edges for both
recommendations = defaultdict(int)

# run dijkstra's on both to find & retrace shortest paths
def dijkstra(adj):
    # this itself will become an adjacency list
    prev = {i: [] for i in range(n)}
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (0, n - 1))
    dist = [float('inf')] * n
    dist[n - 1] = 0
    while len(pq) > 0:
        curD, u = heapq.heappop(pq)
        if curD > dist[u]:
            continue
        for v, w in adj[u]:
            alt = curD + w
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(pq, (alt, v))
                prev[v] = [u]
    # print(prev)
    pathEdges = []
    for i in range(n - 1):
        for j in prev[i]:
            pathEdges.append((i, j))
    for e in pathEdges:
        u, v = e
        recommendations[(u, v)] += 1
dijkstra(adj1)
dijkstra(adj2)
# print(recommendations)

# djikstra's one last time using edge costs
pq = []
heapq.heapify(pq)
heapq.heappush(pq, (0, 0))
dist = [float('inf')] * n
dist[0] = 0
while len(pq) > 0:
    curD, u = heapq.heappop(pq)
    if curD > dist[u]:
        continue
    for v in adj_simple[u]:
        # ignore w, use recommendations to calculate complaints
        w = 2 - recommendations[(u, v)]
        # print(u, v, w)
        alt = curD + w
        if alt < dist[v]:
            dist[v] = alt
            heapq.heappush(pq, (alt, v))            
print(dist[-1])

'''
need to mark edges on all shortest paths
go backwards from the end!
'''
