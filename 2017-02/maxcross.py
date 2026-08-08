import sys
sys.stdin = open("maxcross.in")
sys.stdout = open("maxcross.out", 'w')

n, k, b = map(int, input().split())
blocked = [int(input()) for _ in range(b)]
lights = [0] * n
for block in blocked:
    lights[block - 1] += 1
cur = sum(lights[:k])
ans = cur
for i in range(n - k):
    cur -= lights[i]
    cur += lights[i + k]
    ans = min(ans, cur)
print(ans)
'''
sliding window
'''
