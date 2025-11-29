import sys
sys.stdin = open("cruise.in")
sys.stdout = open("cruise.out", 'w')
input = sys.stdin.readline
from collections import defaultdict

n, m, k = map(int, input().split())
adj = [(2000, 2000)] + [tuple(map(int, input().split())) for _ in range(n)]
# print(adj)
directions = list(input().split())
for i in range(len(directions)):
    if directions[i] == 'L':
        directions[i] = 0
    else:
        directions[i] = 1
# print(directions)

# maps port number to last seen
portIdx = defaultdict(int)
ports = [1]
cur = 1
for i in range(1, 1003):
    for d in directions:
        cur = adj[cur][d]
    if i == k:
        print(cur)
        exit()
    ports.append(cur)
    if portIdx[cur]:
        # cycle found        
        cycleStart = portIdx[cur]
        cycleLength = i - portIdx[cur]
        increment = (k - cycleStart) % cycleLength
        # print(ports, cycleStart, portIdx)
        # print(cycleStart, cycleLength, increment)
        print(ports[cycleStart + increment])
        break
    portIdx[cur] = i
# print(portIdx)
