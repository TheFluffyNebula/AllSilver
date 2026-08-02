import sys
sys.stdin = open("diamond.in")
sys.stdout = open("diamond.out", 'w')

n, k = map(int, input().split())
diamonds = [int(input()) for _ in range(n)]
diamonds.sort()
windowK = []
L = 0
for R in range(n):
    while diamonds[R] - diamonds[L] > k:
        L += 1
    windowK.append((L, R))
# print(windowK)
# suffix maximum
suffixK = []
mx = 0
for i in range(len(windowK) - 1, -1, -1):
    mx = max(mx, windowK[i][1] - windowK[i][0])
    # start location, suffix maximum
    suffixK.append((windowK[i][0], mx))
suffixK.reverse()
# print(suffixK)

best = 0
for firstWindow in range(len(windowK)):
    cur_window_right = windowK[firstWindow][1]
    L = firstWindow
    R = len(windowK) - 1
    secondWindow = -1
    while L <= R:
        mid = (L + R) // 2
        if suffixK[mid][0] > cur_window_right:
            secondWindow = mid
            R = mid - 1
        else:
            L = mid + 1
    if secondWindow != -1:
        # print(firstWindow, secondWindow)
        best = max(best, windowK[firstWindow][1] - windowK[firstWindow][0] + 1 + suffixK[secondWindow][1] + 1)
# now for 2k - 1
L = 0
for R in range(n):
    while diamonds[R] - diamonds[L] > 2 * k - 1:
        L += 1
        if L >= n:
            break
    if L >= n:
        break
    best = max(best, R - L + 1)
print(best)
'''
What if we compute the possible ranges that any one case can hold at a time via 2P?
2 cases:
the optimal arrangement is disjoint
    keep track of the largest two separate cases
the optimal arrangement overlaps
    look over the array w/ a window of 2k - 1

sweep over w/ window k, see where that gets us
might have some overlapping windows, what then?
    idea: suffix maximum for windows
    (starting point, mx)
    could store these in an array, then binary search for "first starting point > cur_window_right"
'''
