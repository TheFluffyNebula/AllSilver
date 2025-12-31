import sys
sys.stdin = open("stampede.in")
sys.stdout = open("stampede.out", 'w')
from collections import defaultdict
import bisect

n = int(input())
cows = [tuple(map(int, input().split())) for _ in range(n)]
# print(cows)

add = defaultdict(list)
rm = defaultdict(list)
pts = set()
# intervals = []
for i in range(n):
    reachZero = -(cows[i][0] + 1) * cows[i][2]
    endZero = reachZero + cows[i][2]
    # intervals.append((reachZero, endZero, cows[i][1]))
    add[reachZero].append(cows[i][1])
    rm[endZero].append(cows[i][1])
    pts.add(reachZero)
    pts.add(endZero)
pts = sorted(list(pts))
# print(pts, add, rm)

seen = set()
window = []
for p in pts:
    put = add[p]
    remove = rm[p]
    if put:
        for insertElment in put:
            bisect.insort(window, insertElment)
    if remove:
        for removeElement in remove:
            # window.remove(removeElement)
            idx = bisect.bisect_left(window, removeElement)
            window.pop(idx)
    if window:
        seen.add(window[0])

# print(seen)
print(len(seen))

'''
cows being represented by line segments make this a lot trickier
is there a way to simulate this quickly?

priority queue/binary tree, smallest one at any time is able to be seen
store by y-coordinates (unique)
add when we get to L, remove when we get to R

ok, I think it's finally time to make a binary tree implementation
'''
