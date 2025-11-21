import sys
# sys.stdin = open("rblock.in")
input = sys.stdin.readline
from queue import PriorityQueue
from collections import defaultdict

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
weights = defaultdict(int)
for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    weights[(a, b)] = w
    weights[(b, a)] = w

dist = [float('inf')] * (n + 1)
dist[1] = 0
pq = PriorityQueue()
pq.put((0, 1))
prev = [-1] * (n + 1)
while not pq.empty():
    cur, u = pq.get()
    if dist[u] == float('inf'):
        continue
    for v in adj[u]:
        alt = cur + weights[(u, v)]
        if alt < dist[v]:
            dist[v] = alt
            pq.put((alt, v))
            prev[v] = u
# print(dist, prev)
bestInitial = dist[n]

edges = []
next = n
cur = prev[next]
while cur != -1:
    edges.append((cur, next))
    next = cur
    cur = prev[next]
# print(edges)

def dijkstra():
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    pq = PriorityQueue()
    pq.put((0, 1))
    while not pq.empty():
        cur, u = pq.get()
        if dist[u] == float('inf'):
            continue
        for v in adj[u]:
            alt = cur + weights[(u, v)]
            if alt < dist[v]:
                dist[v] = alt
                pq.put((alt, v))
    return dist[n]

ans = 0
for edge in edges:
    weights[(edge[0], edge[1])] *= 2
    weights[(edge[1], edge[0])] *= 2
    # print(weights)
    length = dijkstra()
    ans = max(ans, length)
    weights[(edge[0], edge[1])] //= 2
    weights[(edge[1], edge[0])] //= 2
print(ans - bestInitial)

'''
dijkstra's to find shortest path edges
then ans = max(dijkstra's after doubling an edge)
'''
