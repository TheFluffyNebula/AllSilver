import sys
sys.stdin = open("fairphoto.in")
sys.stdout = open("fairphoto.out", 'w')

n = int(input())
cows = [input().split() for _ in range(n)]
for i in range(n):
    val = 1
    if cows[i][1] == "S":
        val = -1
    cows[i] = (int(cows[i][0]), val)
cows.sort()
# print(cows)

pf = [0]
for i in range(n):
    pf.append(pf[-1] + cows[i][1])
odds = []
evens = []
for i in range(n):
    if i % 2 == 0:
        odds.append(pf[i + 1])
    else:
        evens.append(pf[i + 1])
# now suffix maximums to create what we binary search on
cur = float('-inf')
for i in range(len(odds) - 1, -1, -1):
    cur = max(cur, odds[i])
    odds[i] = cur
cur = float('-inf')
for i in range(len(evens) - 1, -1, -1):
    cur = max(cur, evens[i])
    evens[i] = cur
# print(len(odds), len(evens))
# 012345
# 0 1 2
#  0 1 2

def f(i, searchEvens):
    if searchEvens:
        L = i // 2
        R = len(evens) - 1
        x = L
        if x > R:
            return 0
        while L <= R:
            mid = (L + R) // 2
            if evens[mid] >= pf[i + 1]:
                x = mid
                L = mid + 1
            else:
                R = mid - 1
        return cows[2 * x + 1][0] - cows[i][0]
    else:
        L = (i + 1) // 2
        R = len(odds) - 1
        x = L
        if x > R:
            return 0
        while L <= R:
            mid = (L + R) // 2
            if odds[mid] >= pf[i + 1]:
                x = mid
                L = mid + 1
            else:
                R = mid - 1
        return cows[2 * x][0] - cows[i][0]

ans = 0
for i in range(n):
    # i represents the starting index
    searchEvens = True
    if i % 2 == 1:
        searchEvens = False
    candidate = f(i, searchEvens)
    ans = max(ans, candidate)
print(ans)
'''
peeked the solution ;-;
first, compute prefix sums
for each entry (alternate odd/even, store separately)
    binary search on all opposite parity using suffix maximum
    ans = max(ans, candidate)
eventual todo: for the first... toggle attempt?
'''
