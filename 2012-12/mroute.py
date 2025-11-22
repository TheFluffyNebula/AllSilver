import sys
sys.stdin = open("mroute.in")
sys.stdout = open("mroute.out", 'w')
input = sys.stdin.readline
from queue import PriorityQueue

n, m, x = map(int, input().split())
latency = [[float('inf') for _ in range(n)] for _ in range(n)]
cap = [[float('inf') for _ in range(n)] for _ in range(n)]
adj = {i: [] for i in range(n)}
edgelist = []
for _ in range(m):
    i, j, l, c = map(int, input().split())
    i -= 1
    j -= 1
    latency[i][j] = l
    latency[j][i] = l
    cap[i][j] = c
    cap[j][i] = c
    adj[i].append(j)
    adj[j].append(i)
    edgelist.append((i, j, c))

def dijkstra(start, end1, end2, minCapacity):
    # only allowed to take a path if its capacity is >= minCapacity
    dist = [float('inf') for _ in range(n)]
    dist[start] = 0
    pq = PriorityQueue()
    pq.put((0, start))
    while not pq.empty():
        curDist, u = pq.get()
        if u == end1 or u == end2:
            return curDist
        if curDist > dist[u]:
            continue
        for v in adj[u]:
            if cap[u][v] < minCapacity:
                continue
            alt = curDist + latency[u][v]
            if alt < dist[v]:
                dist[v] = alt
                pq.put((alt, v))
    # didn't find a path
    return float('inf')

best = float('inf')
for edge in edgelist:
    # lock this edge as the minimum edge
    fromStart = dijkstra(0, edge[0], edge[1], edge[2])
    fromEnd = dijkstra(n - 1, edge[0], edge[1], edge[2])
    # print(fromStart, fromEnd, edge)
    best = min(best, fromStart + latency[edge[0]][edge[1]] + fromEnd + x / edge[2])
print(int(best))

'''
same concept from Omg Graph: https://codeforces.com/contest/2117/problem/G
lock minimum edge, find shortest paths to it
'''
