from collections import deque

# --- Read input ---
n1, n2, n3 = map(int, input().split())
P = []
for _ in range(3):
    k = [tuple(map(int, input().split())) for __ in range([n1, n2, n3][len(P)])]
    P.append(k)

# --- Normalize each shape into a 10×10 bitmask ---
W = [0]*3
H = [0]*3
A = [[[0]*10 for _ in range(10)] for _ in range(3)]
sx0 = [0]*3
sy0 = [0]*3

for i in range(3):
    pts = P[i]

    # find bounding box
    mnx = min(x for x, y in pts)
    mny = min(y for x, y in pts)
    mxX = max(x for x, y in pts) + 1
    mxY = max(y for x, y in pts) + 1

    W[i] = mxX - mnx
    H[i] = mxY - mny

    # translate points so min corner is (0,0)
    for x, y in pts:
        A[i][x - mnx][y - mny] = 1

    # initial offsets so that original positions are preserved
    sx0[i] = mnx
    sy0[i] = mny


# --- Check bounding-box overlap ---
def bbox_intersect(i, j, dx_i, dy_i, dx_j, dy_j):
    # using global W,H,A arrays; dx_i is offset relative to original
    if dx_i < dx_j + W[j] and dx_j < dx_i + W[i] and \
       dy_i < dy_j + H[j] and dy_j < dy_i + H[i]:
        return True
    return False


# --- Check pixel overlap using bitmasks ---
def shape_overlap(i, j, dx_i, dy_i, dx_j, dy_j):
    # Only call if bounding boxes intersect
    offx = dx_j - dx_i
    offy = dy_j - dy_i
    # Try all cells in i's shape
    for x in range(W[i]):
        for y in range(H[i]):
            if A[i][x][y] == 0:
                continue
            nx = x + offx
            ny = y + offy
            if 0 <= nx < W[j] and 0 <= ny < H[j]:
                if A[j][nx][ny] == 1:
                    return True
    return False


def any_overlap(dx2, dy2, dx3, dy3):
    # shape 1 is at (0,0)
    # shape 2 at (dx2, dy2), shape 3 at (dx3, dy3)
    # Check pair 1-2
    if bbox_intersect(0, 1, 0, 0, dx2, dy2):
        if shape_overlap(0, 1, 0, 0, dx2, dy2):
            return True
    # Check pair 1-3
    if bbox_intersect(0, 2, 0, 0, dx3, dy3):
        if shape_overlap(0, 2, 0, 0, dx3, dy3):
            return True
    # Check pair 2-3
    if bbox_intersect(1, 2, dx2, dy2, dx3, dy3):
        if shape_overlap(1, 2, dx2, dy2, dx3, dy3):
            return True
    return False


# --- BFS with ±20 bounds ---
DIRECTIONS = [
    # Move shape 1 (shift shapes 2+3 inversely)
    (1, 0, 1, 0), (-1, 0, -1, 0),
    (0, 1, 0, 1), (0, -1, 0, -1),
    # Move shape 2
    (1, 0, 0, 0), (-1, 0, 0, 0),
    (0, 1, 0, 0), (0, -1, 0, 0),
    # Move shape 3
    (0, 0, 1, 0), (0, 0, -1, 0),
    (0, 0, 0, 1), (0, 0, 0, -1),
]

start_dx2 = sx0[1] - sx0[0]
start_dy2 = sy0[1] - sy0[0]
start_dx3 = sx0[2] - sx0[0]
start_dy3 = sy0[2] - sy0[0]

q = deque()
q.append((start_dx2, start_dy2, start_dx3, start_dy3, 0))
vis = {(start_dx2, start_dy2, start_dx3, start_dy3)}

while q:
    dx2, dy2, dx3, dy3, d = q.popleft()

    # Goal: no overlaps
    if not any_overlap(dx2, dy2, dx3, dy3):
        print(d)
        break

    # Try all moves
    for d2x, d2y, d3x, d3y in DIRECTIONS:
        ndx2 = dx2 + d2x
        ndy2 = dy2 + d2y
        ndx3 = dx3 + d3x
        ndy3 = dy3 + d3y

        # prune: must stay within [-20,20]
        if abs(ndx2) > 20 or abs(ndy2) > 20 or abs(ndx3) > 20 or abs(ndy3) > 20:
            continue

        st = (ndx2, ndy2, ndx3, ndy3)
        if st not in vis:
            vis.add(st)
            q.append((ndx2, ndy2, ndx3, ndy3, d+1))
else:
    print(-1)
