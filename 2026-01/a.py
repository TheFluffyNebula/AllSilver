import sys
# sys.stdin = open("a.in")
from decimal import Decimal

# where is cow c at time t?
'''
overall path: first stays in spot for awhile, then enters the following cycle:
    move towards position 0 at a rate of 1 position per timestep
first descent to zero begins at time t = 2 * c
'''

def cowPos(c, t):
    # print(c, t)
    # check for inSpot
    if t < 2 * c:
        return c
    time = 2 * c - 1
    if c == 0 or c == 1:
        time = c
    while time < t:
        # print(c, time)
        yIntercept = time + c
        if yIntercept < t:
            time = yIntercept
            c = 0
        else:
            return c - (t - time)
        if c == 0:
            time += 1
            c = time // 2
    return c

'''
for this we have to go backwards!
go until position > t // 2
'''
# what cow is at x at time t?
def cowAtPos(x, t):
    # print(x, t)
    while x <= t // 2:
        # x += 1, t -= 1, find where x == t // 2 --> then x = 0, t -= 1
        # 3x = x + t, round down
        x_after = int((Decimal(x) + Decimal(t)) / 3)
        jumpLength = x_after - x
        t_after = t - jumpLength
        x = x_after
        t = t_after
        if x == t // 2:
            # tp back to zero
            x = 0
            t -= 1
        else:
            return x + 1
    return x

q = int(input())
for query in range(q):
    cmd, cx, t = map(int, input().split())
    if cmd == 1:        
        print(cowPos(cx, t))
    else:
        print(cowAtPos(cx, t))
