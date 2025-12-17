# still TLE
import sys
sys.stdin = open("irrigation.in")
# sys.stdout = open("irrigation.out", 'w')
input = sys.stdin.readline

n, c = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(n)]

key = [float('inf') for _ in range(n)]
inMST = [False for _ in range(n)]
key[0] = 0

ans = 0
for i in range(n):
    u = -1
    for v in range(n):
        if not inMST[v] and (u == -1 or key[v] < key[u]):
            u = v

    if key[u] == float('inf'):
        print(-1)
        exit()
    inMST[u] = True
    ans += key[u]

    for v in range(n):
        alt = (a[u][0] - a[v][0]) ** 2 + (a[u][1] - a[v][1]) ** 2
        if alt < c:
            continue
        if not inMST[v] and alt < key[v]:
            key[v] = alt

print(ans)

'''
alright, Prim's over Kruskal's shaves off a log factor for dense graph
'''
