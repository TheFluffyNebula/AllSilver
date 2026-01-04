# 11/12, TLE
import sys
sys.stdin = open("cowroute.in")
sys.stdout = open("cowroute.out", 'w')
# from queue import PriorityQueue
import heapq
from collections import defaultdict

a, b, numRoutes = map(int, input().split())
a -= 1
b -= 1

routeLengths = [0] * numRoutes
routeCosts = [0] * numRoutes
routes = []

n = 0
for i in range(numRoutes):
    ticketPrice, numCities = map(int, input().split())
    cities = list(map(lambda x: int(x) - 1, input().split()))
    routeLengths[i] = len(cities)
    routeCosts[i] = ticketPrice
    n = max(n, max(cities) + 1)
    routes.append(cities)
# print(routes)

# contains entries from both:
# city to next stop and city to next stop on a different route
# adj[(a, b)] = route a, city b
adj = defaultdict(list)
cityToEntry = [[] for _ in range(n)]
# same route, next stop
for i in range(numRoutes):
    cityToEntry[routes[i][0]].append((i, routes[i][0]))
    for j in range(len(routes[i]) - 1):
        adj[(i, routes[i][j])].append((i, routes[i][j + 1]))
        cityToEntry[routes[i][j + 1]].append((i, routes[i][j + 1]))
# print(adj)
# print(cityToEntry)
adj_different = defaultdict(list)
# different route
for cityNum in range(n):
    numRoutesIn = len(cityToEntry[cityNum])
    # print(cityToEntry[cityNum])
    for i in range(numRoutesIn):
        for j in range(i + 1, numRoutesIn):
            node1 = cityToEntry[cityNum][i]
            node2 = cityToEntry[cityNum][j]
            # exchange entries
            if adj[node2]:
                adj_different[node1].append(adj[node2][0])
            if adj[node1]:
                adj_different[node2].append(adj[node1][0])
# print(adj_different, end="\n\n")
for k, v in adj_different.items():
    for diffRouteStop in v:
        adj[k].append(diffRouteStop)
# print(adj)

# find the optimal route sets
dist = [[(float('inf'), float('inf')) for _ in range(n)] for _ in range(n)]
pq = []
heapq.heapify(pq)
for ent in cityToEntry[a]:
    # route cost, num flights, route/city
    heapq.heappush(pq, (routeCosts[ent[0]], 0, ent))
    # distance initialization: minimum cost as appears in a route
    # dist[ent[1]] = min(dist[ent[1]], routeCosts[ent[0]])
while len(pq):
    curCost, curFlights, routeCityTuple = heapq.heappop(pq)
    routeNum, u = routeCityTuple
    if (curCost, curFlights) > dist[routeNum][u]:
        continue
    for newRCTuple in adj[routeCityTuple]:
        newRouteNum, v = newRCTuple
        alt = curCost
        if routeNum != newRouteNum:
            alt += routeCosts[newRouteNum]
        if (alt, curFlights + 1) < dist[newRouteNum][v]:
            dist[newRouteNum][v] = (alt, curFlights + 1)
            heapq.heappush(pq, (alt, curFlights + 1, newRCTuple))
# print(dist, prev)
best = (float('inf'), float('inf'))
for i in range(numRoutes):
    if dist[i][b] < best:
        best = dist[i][b]        
minCost, flights = best
if minCost == float('inf'):
    print(-1, -1)
else:
    print(minCost, flights)

'''
dijkstra's
hopping onto a new route costs something
continuing on the same route costs
use prev array to get the least flights to transfer

wait... I think I have to do all of this in two dimensions
'''
