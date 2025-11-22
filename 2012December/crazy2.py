# fixing runtime errors
import sys
sys.stdin = open("crazy.in")
sys.stdout = open("crazy.out", 'w')
input = sys.stdin.readline
from collections import defaultdict, Counter

n, c = map(int, input().split())
segments = []
ptsToIdx = defaultdict(int)
idxToPts = defaultdict(tuple)
for i in range(1, n + 1):
    x1, y1, x2, y2 = map(int, input().split())
    segments.append((x1, y1, x2, y2))
    if ptsToIdx[(x1, y1)] == 0:
        ptsToIdx[(x1, y1)] = len(ptsToIdx)
        idxToPts[len(ptsToIdx)] = (x1, y1)
    if ptsToIdx[(x2, y2)] == 0:
        ptsToIdx[(x2, y2)] = len(ptsToIdx)
        idxToPts[len(ptsToIdx)] = (x2, y2)
# print(segments)
# print(idxToPts)

adj = {i: [] for i in range(n)}
for segment in segments:
    a = ptsToIdx[(segment[0], segment[1])]
    b = ptsToIdx[(segment[2], segment[3])]
    a, b = a - 1, b - 1
    adj[a].append(b)
    adj[b].append(a)
# print(adj)

visited = [False] * n
def dfs(i):
    shape = []
    stack = [i]
    visited[i] = True
    while stack:
        u = stack.pop()
        shape.append(idxToPts[u + 1])
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    shapes.append(shape)

shapes = []
# make the shapes
for i in range(n):
    if not visited[i]:
        dfs(i)
# print(shapes)

shapeAreas = defaultdict(int)
for (i, shape) in enumerate(shapes):
    x1 = 0
    x2 = 0
    for j in range(len(shape)):
        x1 += shape[j][0] * shape[(j + 1) % len(shape)][1]
        x2 += shape[j][1] * shape[(j + 1) % len(shape)][0]
    area = 0.5 * abs(x1 - x2)
    shapeAreas[i] = area
# print(shapeAreas)

cows = [tuple(map(int, input().split())) for _ in range(c)]

shapeStatus = [-1] * c
# print(shapeStatus)

def pointInPolygon(cow, shape):
    hits = 0
    # does a ray from (cx, cy) intersect (f1, f2)?
    cx, cy = cow
    for i in range(len(shape)):
        p1, p2 = shape[i], shape[(i + 1) % len(shape)]
        f1x, f1y = p1
        f2x, f2y = p2
        if ((f1y > cy) ^ (f2y > cy)):
            hits += (f1y - f2y < 0) ^ (f2x * (f1y - cy) + f1x * (cy - f2y) > cx * (f1y - f2y));
        else:
            continue
    return hits % 2 == 1

for (i, cow) in enumerate(cows):
    leastArea = float('inf')
    leastIdx = -1
    for (j, shape) in enumerate(shapes):
        if pointInPolygon(cow, shape):
            if shapeAreas[j] < leastArea:
                leastArea = shapeAreas[j]
                leastIdx = j
    shapeStatus[i] = leastIdx
print(max(Counter(shapeStatus).values()))

'''
1. mark what shape it's in (in-no-shape is its own)
    point in polygon
    innermost polygon --> least area of those in, shoelace theorem
2. ans = max(shapes)

point in polygon... copied the "ray tracing algorithm"
'''
