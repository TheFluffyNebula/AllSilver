import sys
sys.stdin = open("rblock.in")
sys.stdout = open("rblock.out", 'w')
from queue import PriorityQueue

n, m = map(int, input().split())
adj = {i: [] for i in range(n)}
for i in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append((b, w))
    adj[b].append((a, w))

dist = [float('inf')] * n
prev = [0] * n
dist[0] = 0
pq = PriorityQueue()
pq.put((0, 0))
while not pq.empty():
    curD, u = pq.get()
    if curD > dist[u]:
        continue
    for v, w in adj[u]:
        alt = dist[u] + w
        if alt < dist[v]:
            prev[v] = u
            dist[v] = alt
            pq.put((alt, v))
before = dist[n - 1]
# print(prev)
# print(dist)

def dijkstra(double1, double2):
    dist = [float('inf')] * n
    dist[0] = 0
    pq = PriorityQueue()
    pq.put((0, 0))
    while not pq.empty():
        curD, u = pq.get()
        if curD > dist[u]:
            continue
        for v, w in adj[u]:
            alt = dist[u] + w
            if (u == double1 and v == double2) or (u == double2 and v == double1):
                alt += w
            if alt < dist[v]:
                dist[v] = alt
                pq.put((alt, v))
    return dist[n - 1]

p = []
cur = n - 1
while cur:
    p.append(cur)
    cur = prev[cur]
p.append(0)
# print(p)

after = 0
for i in range(len(p) - 1):
    # print(p[i], p[i + 1])
    after = max(after, dijkstra(p[i], p[i + 1]))
print(after - before)

'''
try doubling each edge on the shortest path
'''
