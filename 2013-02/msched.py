import sys
sys.stdin = open("msched.in")
sys.stdout = open("msched.out", 'w')
from collections import deque

n, m = map(int, input().split())
times = [0] * n
for i in range(n):
    times[i] = int(input())
# print(times)
indegree = [0] * n
adj = {i: [] for i in range(n)}
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    indegree[b] += 1

# base distance, these will go up
dist = [times[i] for i in range(n)]
# those that have no dependencies start
q = deque()
for i in range(n):
    if indegree[i] == 0:
        q.append(i)
# bfs
while q:
    u = q.popleft()
    for v in adj[u]:
        indegree[v] -= 1
        dist[v] = max(dist[v], dist[u] + times[v])
        if indegree[v] == 0:
            # all previous cows are done!
            q.append(v)

print(max(dist))

'''
some ideas:
1. direct simulation (probably too slow)

2. topological sort (not really, more like select degrees w/ 0 in-degree)
    ans = longest path: (node takes max of any path to it)
    use indegree to identify when nodes are ready
'''
