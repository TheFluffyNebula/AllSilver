# asked Claude again here, cool lambda function use!
import sys
sys.stdin = open("reduce.in")
sys.stdout = open("reduce.out", 'w')

def area(pts):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return (max(xs) - min(xs)) * (max(ys) - min(ys))

def search(pts, k):
    global ans
    ans = min(ans, area(pts))
    if k == 0:
        return
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    extremes = [
        lambda p, v=min(xs): p[0] == v,
        lambda p, v=max(xs): p[0] == v,
        lambda p, v=min(ys): p[1] == v,
        lambda p, v=max(ys): p[1] == v,
    ]
    for is_extreme in extremes:
        cost = sum(1 for p in pts if is_extreme(p))
        if cost <= k:
            search([p for p in pts if not is_extreme(p)], k - cost)

n = int(input())
cows = [tuple(map(int, input().split())) for _ in range(n)]
ans = float('inf')
search(cows, 3)
print(ans)