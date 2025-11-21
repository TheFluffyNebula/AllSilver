# heapq speedup of 3x was enough
import sys
sys.stdin = open("distant.in")
sys.stdout = open("distant.out", 'w')
input = sys.stdin.readline
# from queue import PriorityQueue
import heapq

n, a, b = map(int, input().split())
farm = [input().strip() for _ in range(n)]
# print(farm)

adj = {}
for i in range(n):
    for j in range(n):
        adj_list = []
        if i > 0:
            if farm[i][j] == farm[i - 1][j]:
                adj_list.append((a, (i - 1, j)))
            else:
                adj_list.append((b, (i - 1, j)))
        if i < n - 1:
            if farm[i][j] == farm[i + 1][j]:
                adj_list.append((a, (i + 1, j)))
            else:
                adj_list.append((b, (i + 1, j)))
        if j > 0:
            if farm[i][j] == farm[i][j - 1]:
                adj_list.append((a, (i, j - 1)))
            else:
                adj_list.append((b, (i, j - 1)))
        if j < n - 1:
            if farm[i][j] == farm[i][j + 1]:
                adj_list.append((a, (i, j + 1)))
            else:
                adj_list.append((b, (i, j + 1)))
        adj[(i, j)] = adj_list
# print(adj)

def dijkstra(startX, startY):
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    dist[startX][startY] = 0
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (0, (startX, startY)))
    while pq:
        curDist, (curX, curY) = heapq.heappop(pq)
        if curDist > dist[curX][curY]:
            continue
        for w, (newX, newY) in adj[(curX, curY)]:
            alt = dist[curX][curY] + w
            if alt < dist[newX][newY]:
                dist[newX][newY] = alt
                heapq.heappush(pq, (alt, (newX, newY)))
    mx = 0
    for i in range(n):
        for j in range(n):
            mx = max(mx, dist[i][j])
    return mx

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dijkstra(i, j))
print(ans)

'''
brute force dijkstra's
'''
