# TLE, 7/10
import sys
sys.stdin = open("irrigation.in")
# sys.stdout = open("irrigation.out", 'w')

n, c = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(n)]

class DSU:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.sizes = [1 for i in range(size)]
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
        if self.sizes[yr] > self.sizes[xr]:
            xr, yr = yr, xr
        self.parents[yr] = xr
        self.sizes[xr] += self.sizes[yr]
        return True

edges = []
for i in range(n):
    for j in range(i + 1, n):
        w = (a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2
        edges.append((w, i, j))
edges.sort()

d = DSU(n)
ans = 0
for e in edges:
    w, a, b = e
    if w < c:
        continue
    if d.find(a) != d.find(b):
        ans += w
        d.unite(a, b)
if max(d.sizes) == n:
    print(ans)
else:
    print(-1)
