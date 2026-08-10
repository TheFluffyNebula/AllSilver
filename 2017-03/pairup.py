import sys
sys.stdin = open("pairup.in")
sys.stdout = open("pairup.out", 'w')

n = int(input())
cows = [tuple(map(int, input().split())) for _ in range(n)]
cows.sort(key=lambda x: x[1])
# print(cows)

L = 0
R = n - 1
lCount = cows[L][0]
rCount = cows[R][0]
ans = 0
while L < R:
    tot = cows[L][1] + cows[R][1]
    ans = max(ans, tot)
    subtract = min(lCount, rCount)
    lCount -= subtract
    rCount -= subtract
    if lCount == 0:
        L += 1
        lCount = cows[L][0]
    if rCount == 0:
        R -= 1
        rCount = cows[R][0]
if L == R:
    ans = max(ans, cows[L][1] + cows[R][1])
print(ans)

'''
always want to pair low and high
simulate fast. 2P, left and right.
'''
