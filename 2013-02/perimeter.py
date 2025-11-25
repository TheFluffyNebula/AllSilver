import sys
sys.stdin = open("perimeter.in")
sys.stdout = open("perimeter.out", 'w')
from collections import defaultdict, deque

n = int(input())
minX, minY = float('inf'), float('inf')
p = []
present = defaultdict(int)
startPoint = (-1, -1)
for _ in range(n):
    a, b = map(int, input().split())
    minX = min(minX, a)
    minY = min(minY, b)
    if b == minY:
        startPoint = (a, b - 1)
    p.append((a, b))
    present[(a, b)] = 1
# print(p)
# print(startPoint)

# track the boxes that are out
out = defaultdict(int)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# (-1, 0) is guaranteed to be outside
out[startPoint] = 1
q = deque()
q.append(startPoint)
while q:
    # flood in four directions, check in eight
    curX, curY = q.popleft()
    for dx, dy in DIRECTIONS:
        x, y = curX + dx, curY + dy
        # if out[(x, y)]:
        if (x, y) in out or present[(x, y)]:
            continue
        # prune
        if present[(x + 1, y)] + present[(x + 1, y + 1)] + present[(x, y + 1)] + present[(x - 1, y + 1)] \
        + present[(x - 1, y)] + present[(x - 1, y - 1)] + present[(x, y - 1)] + present[(x + 1, y - 1)] == 0:
            continue
        out[(x, y)] = 1
        q.append((x, y))
# print(out)

ans = 0
for pt in p:
    px, py = pt
    ans += out[(px + 1, py)]
    ans += out[(px - 1, py)]
    ans += out[(px, py - 1)]
    ans += out[(px, py + 1)]
print(ans)
'''
analyze
attempt 1
only the ones on the outside contribute to perimeter
    leftmost/rightmost in a row, topmost/botmost in a column
    leftmost contribute +1 left, topmost contribute +1 top...
is it that simple? all extremes contribute +1
nvm, have to track all outside points
traversal could be tricky

attempt 2
flood fill, better gets those on the perimeter
'''
