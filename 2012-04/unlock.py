import sys
# sys.stdin = open("unlock.in")
input = sys.stdin.readline
from collections import deque

n1, n2, n3 = map(int, input().split())
p1, p2, p3 = [], [], []
for _ in range(n1):
    a, b = map(int, input().split())
    p1.append((a, b))
for _ in range(n2):
    a, b = map(int, input().split())
    p2.append((a, b))
for _ in range(n3):
    a, b = map(int, input().split())
    p3.append((a, b))
# print(p1, p2, p3)

# compute initial boxes for convenience
# minX, maxX, minY, maxY
def create_box(pts):
    minX, maxX, minY, maxY = float('inf'), float('-inf'), float('inf'), float('-inf')
    for x, y in pts:
        minX = min(minX, x)
        maxX = max(maxX, x + 1)
        minY = min(minY, y)
        maxY = max(maxY, y + 1)
    return [minX, maxX, minY, maxY]
box1 = create_box(p1)
box2 = create_box(p2)
box3 = create_box(p3)
# print(box1, box2, box3)

# p2_x, p2_y, p3_x, p3_y
DIRECTIONS = [
    # p1 movements
    (1, 0, 1, 0), (-1, 0, -1, 0), (0, 1, 0, 1), (0, -1, 0, -1), 
    # p2 movements
    (1, 0, 0, 0), (-1, 0, 0, 0), (0, 1, 0, 0), (0, -1, 0, 0), 
    # p3 movements
    (0, 0, 1, 0), (0, 0, -1, 0), (0, 0, 0, 1), (0, 0, 0, -1)
]

# is this a solution?
def verify(a, b, c, d):
    # overlap between p1/p2, p1/p3, p2/p3 --> invalid
    # overlap formula: max[min(x1_max, x2_max) - max(x1_min, x2_min), 0]
    # positive overlap in both = overlap
    # p1/p2
    overlapX = max((min(box1[1], box2[1] + a) - max(box1[0], box2[0] + a)), 0)
    overlapY = max((min(box1[3], box2[3] + b) - max(box1[2], box2[2] + b)), 0)
    if overlapX > 0 and overlapY > 0:
        return False
    # p1/p3
    overlapX = max((min(box1[1], box3[1] + c) - max(box1[0], box3[0] + c)), 0)
    overlapY = max((min(box1[3], box3[3] + d) - max(box1[2], box3[2] + d)), 0)
    if overlapX > 0 and overlapY > 0:
        return False
    # p2/p3
    overlapX = max((min(box2[1] + a, box3[1] + c) - max(box2[0] + a, box3[0] + c)), 0)
    overlapY = max((min(box2[3] + b, box3[3] + d) - max(box2[2] + b, box3[2] + d)), 0)
    if overlapX > 0 and overlapY > 0:
        return False
    # print('hi')
    return True


# is this allowed?
def valid(a, b, c, d):
    # p1/p2
    for p1x, p1y in p1:
        for p2x, p2y in p2:
            if p1x == p2x + a and p1y == p2y + b:
                return False
    # p1/p3
    for p1x, p1y in p1:
        for p3x, p3y in p3:
            if p1x == p3x + c and p1y == p3y + d:
                return False
    # p2/p3
    for p2x, p2y in p2:
        for p3x, p3y in p3:
            if p2x + a == p3x + c and p2y + b == p3y + d:
                return False
    return True

past = set()
q = deque()
q.append((0, 0, 0, 0, 0))
past.add((0, 0, 0, 0))
while q:
    a, b, c, d, dist = q.popleft()
    if verify(a, b, c, d):
        # print(a, b, c, d)
        print(dist)
        exit()
    for da, db, dc, dd in DIRECTIONS:
        newA, newB, newC, newD = a + da, b + db, c + dc, d + dd
        if abs(newA) > 20 or abs(newB) > 20 or abs(newC) > 20 or abs(newD) > 20:
            continue
        if (newA, newB, newC, newD) in past:
            continue
        past.add((newA, newB, newC, newD))
        if valid(newA, newB, newC, newD):
            q.append((newA, newB, newC, newD, dist + 1))
print(-1)

'''
solution peek: bfs
key step: pruning (will never have to move more than 20 spaces)
'''
