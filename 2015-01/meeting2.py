# still TLE
import sys
sys.stdin = open("meeting.in")
sys.stdout = open("meeting.out", 'w')

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

# topological sort to determine traversal order (don't want to miss anything)
stack = [0]
ordering = [0]
visited = [False] * n
visited[0] = True
while stack:
    u = stack.pop()
    for v, _ in adj1[u]:
        if not visited[v]:
            visited[v] = True
            stack.append(v)
            ordering.append(v)

# (u, t)
reachable = [[False for _ in range(100 * (n - 1))] for _ in range(n)]
reachable2 = [[False for _ in range(100 * (n - 1))] for _ in range(n)]
reachable[0][0] = True
reachable2[0][0] = True
for u in ordering:
    if u == n - 1:
        continue
    # iterate from the the end since we're only taking each path once
    endVal = 100 * (n - 1) - 1
    for v, w in adj1[u]:
        for i in range(endVal, -1, -1):
            if i - w < 0:
                break
            reachable[v][i] |= reachable[u][i - w]
    for v, w in adj2[u]:
        for i in range(endVal, -1, -1):
            if i - w < 0:
                break
            reachable2[v][i] |= reachable2[u][i - w]
for i in range(100 * (n - 1)):
    if reachable[n - 1][i] and reachable2[n - 1][i]:
        print(i)
        exit()
print("IMPOSSIBLE")

'''
knapsack-like dp approach
'''
