# copying the editorial
import sys
sys.stdin = open("helpcross.in")
sys.stdout = open("helpcross.out", 'w')
from heapq import *

c, n = map(int, input().split())
chickens = [int(input()) for _ in range(c)]
cows = [tuple(map(int, input().split())) for _ in range(n)]
cows.sort()
chickens.sort()
# print(cows, chickens)

ans = 0
heap = []
i = 0
for ch in chickens:
    while i < n and cows[i][0] <= ch:
        heappush(heap, cows[i][1])
        i += 1
    while heap and heap[0] < ch:
        heappop(heap)
    if heap:
        heappop(heap)
        ans += 1
print(ans)
