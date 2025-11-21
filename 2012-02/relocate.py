import sys
# sys.stdin = open("relocate.in")
input = sys.stdin.readline
from queue import PriorityQueue
from itertools import permutations
from collections import defaultdict

n, m, k = map(int, input().split())
markets = [int(input()) - 1 for _ in range(k)]
# print(markets)
marketToIdx = defaultdict(int)
for i in range(k):
    marketToIdx[markets[i]] = i
# print(marketToIdx)
adj = {i: [] for i in range(n)}
for i in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append((w, b))
    adj[b].append((w, a))

# dist 1, dist 2, dist 3, dist 4, dist 5
marketDistances = [[float('inf') for _ in range(n)] for _ in range(k)]
# print(marketDistances)
def dijkstra(d, start):
    d[start] = 0
    pq = PriorityQueue()
    pq.put((0, start))
    while not pq.empty():
        dist, cur = pq.get()
        if dist > d[cur]:
            continue
        for w, v in adj[cur]:
            alt = d[cur] + w
            if alt < d[v]:
                d[v] = alt
                pq.put((alt, v))
    return

for (i, m) in enumerate(markets):
    dijkstra(marketDistances[i], m)
# print(marketDistances)

best = float('inf')
for p in permutations(markets):
    # print(p)
    marketTravel = 0
    for i in range(k):
        if i == 0:
            continue
        prevIdx = marketToIdx[p[i - 1]]
        # KEY: market index to regular node
        curIdx = p[i]
        marketTravel += marketDistances[prevIdx][curIdx]
    # print(marketTravel, p)
    nonMarketTravel = float('inf')
    for i in range(n):
        if i in markets:
            continue
        nonMarketTravel = min(nonMarketTravel, marketDistances[marketToIdx[p[0]]][i] + marketDistances[marketToIdx[p[k - 1]]][i])
    # print(marketTravel, nonMarketTravel)
    best = min(best, marketTravel + nonMarketTravel)

print(best)

'''
an invariant: he always has to go to all markets and then back
can we, for the 120 possible tours of the up-to-5 markets, get the distance to 
wait, yes, yes! so, we do dijkstra's from each of the 5 markets to everything
(maintain dist for all markets)
then, we take min for each:
    dist + marketTour + distBack
'''
