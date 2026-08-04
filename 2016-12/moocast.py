import sys
sys.stdin = open("moocast.in")
sys.stdout = open("moocast.out", 'w')

n = int(input())
cows = [tuple(map(int, input().split())) for _ in range(n)]
# print(cows)

adj = {i: [] for i in range(n)}
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        # can we get from i to j?
        distance = (cows[i][0] - cows[j][0]) ** 2 + (cows[i][1] - cows[j][1]) ** 2
        if cows[i][2] ** 2 >= distance:
            adj[i].append(j)
# print(adj)

def dfs(start):
    ret = 1
    visited = [False] * n
    visited[start] = True
    stack = [start]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
                ret += 1
    return ret

ans = 0
for i in range(n):
    ans = max(ans, dfs(i))
print(ans)
