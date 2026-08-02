# asked Claude to simplify
# 1. can use disjoint anyway (includes 2k-1 case)
# 2. as I suspected direct suffix lookup was also doable (shaves off log n)
import sys
sys.stdin = open("diamond.in")
sys.stdout = open("diamond.out", 'w')
n, k = map(int, input().split())
d = sorted(int(input()) for _ in range(n))

# window[L] = size of the largest case starting at L
window = [0] * n
R = 0
for L in range(n):
    R = max(R, L)
    while R + 1 < n and d[R + 1] - d[L] <= k:
        R += 1
    window[L] = R - L + 1

# best[i] = max window size for any starting position >= i
best = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    best[i] = max(best[i + 1], window[i])

ans = 0
for L in range(n):
    next_start = L + window[L]  # first index not in the case starting at L
    ans = max(ans, window[L] + best[next_start])

print(ans)
