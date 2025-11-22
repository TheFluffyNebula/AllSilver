import sys
sys.stdin = open("paint.in")
# sys.stdout = open("paint.out", 'w')
input = sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())

# points of interest
poi = defaultdict(int)
intervals = []
pos = 0
for _ in range(n):
    x, d = input().split()
    x = int(x)
    if d == 'R':
        next = pos + x
        intervals.append((pos, next))
    else:
        next = pos - x
        intervals.append((next, pos))
    poi[min(pos, next)] += 1
    poi[max(pos, next)] -= 1
    pos = next
# print(intervals)
# print(poi)
poi_sorted = []
for key, value in poi.items():
    poi_sorted.append((key, value))
poi_sorted.sort()
# print(poi_sorted)

ans = 0
cur = 0
for i in range(len(poi_sorted)):
    cur += poi_sorted[i][1]
    if i < len(poi_sorted) - 1:
        if cur >= k:
            # print(cur, k, cur >= k)
            # print(poi_sorted[i - 1][0], poi_sorted[i][0])
            ans += poi_sorted[i + 1][0] - poi_sorted[i][0]
print(ans)
'''
accumulation + coordinate compression (more like points of interest)
'''
