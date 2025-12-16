# Kruskal's? Full AC, Yippee!
import sys
sys.stdin = open("ccski.in")
sys.stdout = open("ccski.out", 'w')

m, n = map(int, input().split())
course = [list(map(int, input().split())) for _ in range(m)]
waypoints = [list(map(int, input().split())) for _ in range(m)]
# print(*course, sep='\n')
# print(*waypoints, sep='\n')

waypointCount = sum([sum(waypoints[i]) for i in range(m)])
# print(waypointCount)

class DSU:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.sizes = [waypoints[(i // n)][i % n] for i in range(size)]
    
    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def unite(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False

        if self.sizes[xr] < self.sizes[yr]:
            xr, yr = yr, xr
        self.parents[yr] = xr
        self.sizes[xr] += self.sizes[yr]
        if self.sizes[xr] == waypointCount:
            return True
        return False

edges = []
for i in range(m):
    for j in range(n):
        if i > 0:
            w = abs(course[i - 1][j] - course[i][j])
            edges.append((w, (i - 1) * n + j, i * n + j))
        if j > 0:
            w = abs(course[i][j - 1] - course[i][j])
            edges.append((w, i * n + j - 1, i * n + j))
edges.sort()

d = DSU(m * n)

for e in edges:
    w, u, v = e
    if d.find(u) != d.find(v):
        if d.unite(u, v):
            print(w)
            exit()
