# linear n**2 implementation
import sys
sys.stdin = open("painting.in")
# sys.stdout = open("painting.out", 'w')
input = sys.stdin.readline
from collections import defaultdict
import bisect

n = int(input())
r = [tuple(map(int, input().split())) for _ in range(n)]
# sort by startX
r.sort()
# print(r)

start = defaultdict(list)
end = defaultdict(list)
events = set()
for i in range(n):
    x1, y1, x2, y2 = r[i]
    start[x1].append(i)
    end[x2].append(i)
    events.add(x1)
    events.add(x2)
events = sorted(list(events))
# print(events)

# debug array, actual data will be added/removed to a BST
active = [False] * n
# print(start, end)

#REPLACE WITH BST#
edges = []
##################

ans = 0
for e in events:
    for endIdx in end[e]:
        if active[endIdx]:
            active[endIdx] = False
            edges.remove((r[endIdx][1], 1))
            edges.remove((r[endIdx][3], 0))
    # print(edges)

    rm = []
    # for each new entry, if new isn't enclosed, ans += 1
    # "hits top edge before a bottom edge = enclosed"
    for startIdx in start[e]:
        nearestEdge = bisect.bisect(edges, (r[startIdx][1], -1))
        # print(nearestEdge, startIdx)
        if nearestEdge < len(edges) and edges[nearestEdge][1] == 0:
            # enclosed
            pass
        else:
            ans += 1
            active[startIdx] = True
            bisect.insort(edges, (r[startIdx][1], 1))
            bisect.insort(edges, (r[startIdx][3], 0))
    # print(active)
print(ans)
'''
solution peek: sweep line w/ tree
(x1, y1, x2, y2)
'''
