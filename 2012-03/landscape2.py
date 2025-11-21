import sys
# sys.stdin = open("landscape.in")
input = sys.stdin.readline

n, x, y, z = map(int, input().split())
a = []
for i in range(n):
    c, b = map(int, input().split())
    a.append(c - b)
# print(a)

# for any distances greater than this we should use x & y instead of moving
# ex. x = 5, y = 5, z = 7 --> 1 good, 2 bad
d = (x + y) // z
# print("d:", d)

positive = []
negative = []
for i in range(n):
    if a[i] > 0:
        positive.append(i)
    elif a[i] < 0:
        negative.append(i)

movementCost = 0
movement = True
while movement:
    # print(slots)
    movement = False
    if len(positive) == 0 or len(negative) == 0:
        break

    posPtr = 0
    negPtr = 0
    while posPtr < len(positive) and negPtr < len(negative):
        if abs(positive[posPtr] - negative[negPtr]) <= d:
            pIdx = positive[posPtr]
            nIdx = negative[negPtr]
            movement = True
            amt = min(abs(a[pIdx]), abs(a[nIdx]))
            movementCost += amt * abs(pIdx - nIdx) * z
            a[pIdx] -= amt
            a[nIdx] += amt
            if a[pIdx] == 0:
                posPtr += 1
            else:
                negPtr += 1
        else:
            if positive[posPtr] < negative[negPtr]:
                posPtr += 1
            else:
                negPtr += 1

    # update active slots
    positive = []
    negative = []
    for i in range(n):
        if a[i] > 0:
            positive.append(i)
        elif a[i] < 0:
            negative.append(i)
# print(a)
fillRemoveCost = 0
for i in range(n):
    if a[i] < 0:
        fillRemoveCost += abs(a[i]) * x
    else:
        fillRemoveCost += abs(a[i]) * y

ans = movementCost + fillRemoveCost
print(ans)

'''
an idea: when using x & y is strictly better than z * dist
if 1 * z < (x + y) < 2 * z, then for dirt movement >= than 2, we should always choose x & y
let d = (x + y) // z

a strategy:
move first (where it beats fill/remove), fill/remove second
the question remains -- when moving is better, how to best move dirt around?
to clarify, a move is better when (a) opposite signs and (b) smaller distance than d

ok, O(n^2) loop is too slow, have to be a bit smarter about it
O(n) w/ 2P should be fast enough
'''
