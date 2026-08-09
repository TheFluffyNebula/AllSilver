import sys
sys.stdin = open("moocast.in")
sys.stdout = open("moocast.out", 'w')

n = int(input())
cords = [tuple(map(int, input().split())) for _ in range(n)]
# print(cords)

# unvisited cost
unvisited = [float('inf')] * n
# setup the first run
unvisited[0] = 0
visited = [False] * n

greatestEdge = 0
for _ in range(n):
    minIdx = -1
    least = float('inf')
    for i in range(n):
        if not visited[i] and unvisited[i] < least:
            least = unvisited[i]
            minIdx = i
    # visit the node
    visited[minIdx] = True
    greatestEdge = max(greatestEdge, least)
    # recompute the array for other nodes
    for i in range(n):
        weight = (cords[i][0] - cords[minIdx][0]) ** 2 + (cords[i][1] - cords[minIdx][1]) ** 2
        unvisited[i] = min(unvisited[i], weight)
print(greatestEdge)
'''
is it not just MST?
iterative version for true O(n^2) since extra log(n) would TLE
heapless prim's, going to try implementing it myself this time!

"maintains an array (min_weight) storing the cheapest edge weight to connect each unvisited vertex to the current tree."
'''
