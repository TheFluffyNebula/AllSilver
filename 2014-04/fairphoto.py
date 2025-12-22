# 4/10, WA
import sys
sys.stdin = open("fairphoto.in")
# sys.stdout = open("fairphoto.out", 'w')

n = int(input())
cows = [input().split() for _ in range(n)]
cows = [(int(cows[i][0]), cows[i][1]) for i in range(n)]
cows.sort()
# print(cows)

# white - spotted
d = 0
L = 0
ans = 0
for R in range(n):
    if cows[R][1] == "W":
        d += 1
    else:
        d -= 1
    while d < 0 and L < R:
        if cows[L][1] == "W":
            d += 1
        else:
            d -= 1
        L += 1
    if (R - L + 1) % 2 == 0:
        ans = max(ans, cows[R][0] - cows[L][0])
    # print(L, R)
print(ans)

'''
2P
1. white >= spotted
2. numCows is even
ok, not quite (sometimes worth including a negative range for more distance)

with n <= 100,000... we could technically binary search on [1, 50,000] * 2
15 * 100k = 1.5m
let's give it a go
'''
