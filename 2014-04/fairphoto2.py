# 5/10, WA
import sys
sys.stdin = open("fairphoto.in")
# sys.stdout = open("fairphoto.out", 'w')

n = int(input())
cows = [input().split() for _ in range(n)]
cows = [(int(cows[i][0]), cows[i][1]) for i in range(n)]
cows.sort()
# print(cows)

def f(x):
    intervalLength = 2 * x
    d = 0
    for i in range(intervalLength):
        if cows[i][1] == "W":
            d += 1
        else:
            d -= 1
    best = 0
    if d >= 0:
        best = cows[intervalLength - 1][0] - cows[0][0]
    for i in range(n - intervalLength):
        if cows[intervalLength + i][1] == "W":
            d += 1
        else:
            d -= 1
        if cows[i][1] == "W":
            d -= 1
        else:
            d += 1
        if d >= 0:
            best = max(best, cows[intervalLength + i - 1][0] - cows[i][0])
    return best

# multiply actual window size by 2 to guarantee even-ness
L = 1
R = n // 2
ans = 0
while L <= R:
    mid = (L + R) // 2
    x = f(mid)
    # nonzero return value means we found something!
    if x:
        ans = max(ans, x)
        L = mid + 1
    else:
        R = mid - 1
print(ans)

'''
binary search on interval length
if an interval of y then y - 2 better also work
nvm... it's binary search but on something else
'''
