import sys
sys.stdin = open("delivery.in")
input = sys.stdin.readline

n = int(input())
farms = [tuple(map(int, input().split())) for _ in range(n)]
print(farms)

# Returns whether the first point (x1, y1) is on the segment (x2, y2) -> (x3, y3).
def in_segment(x1, y1, x2, y2, x3, y3):
    if x2 == x3:
        return x1 == x2 and y1 > min(y2, y3) and y1 < max(y2, y3)
    elif y2 == y3:
        return y1 == y2 and x1 > min(x2, x3) and x1 < max(x2, x3)
    return True

def possible(ptA, ptB, i, j):
    # check that ptA is not on non-i farm, ptB is not on non-j farm
    for k in range(n):
        if k == i:
            continue
        if ptA == farms[k]:
            return False
    for k in range(n):
        if k == j:
            continue
        if ptB == farms[k]:
            return False
    # now make sure no non-i and non-j farms are on at least one of the paths (horizontal first, vertical first)
    good1, good2 = True
    # horizontal, then vertical
    
    if good1:
        return True
    
    if good2:
        return True
    return False

def shortest_path(idx1, idx2):
    nodes1 = []
    nodes2 = []
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            if a == 0 and b == 0:
                nodes1.append((farms[idx1][0], farms[idx1][1]))
                nodes2.append((farms[idx2][0], farms[idx2][1]))
            elif a * b == 0:
                nodes1.append((farms[idx1][0] + a, farms[idx1][1] + b))
                nodes2.append((farms[idx2][0] + a, farms[idx2][1] + b))
    # print(nodes1, nodes2)

    best = float('inf')
    for n1 in nodes1:
        for n2 in nodes2:
            if possible(n1, n2, idx1, idx2):
                best = min(best, abs(n1[0] - n2[0]) + abs(n1[1] - n2[1]))
    return best

ans = 0
for i in range(n):
    ans += shortest_path(i, (i + 1) % n)

if ans == float('inf'):
    print(-1)
else:
    print(ans)

'''
;-;
sol peek: 5N nodes/edges, use right-angle paths
'''
