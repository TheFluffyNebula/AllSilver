import sys
sys.stdin = open("closing.in")
sys.stdout = open("closing.out", 'w')
input = sys.stdin.readline

def checkConnected(tot):
    for i in range(n):
        if not banned[i]:
            start = i
            break
    visited = [False] * n
    visited[start] = True
    c = 1
    stack = [start]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if banned[v]:
                continue
            if not visited[v]:
                visited[v] = True
                stack.append(v)
                c += 1
    if c == tot:
        print("YES")
    else:
        print("NO")

n, m = map(int, input().split())
adj = {i: [] for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

banned = [False] * n
checkConnected(n)
for i in range(n - 1):
    x = int(input())
    banned[x - 1] = True
    checkConnected(n - i - 1)

'''
simulate the problem. 
'''
