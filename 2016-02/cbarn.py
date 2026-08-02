import sys
sys.stdin = open("cbarn.in")
# sys.stdout = open("cbarn.out", 'w')

n = int(input())
cows = [int(input()) for _ in range(n)]
# print(cows)

def checkEnd(endIdx):
    c = cows.copy()
    sparePtr = -1
    cost = 0
    for i in range(n):
        idx = (endIdx - i) % n
        if c[idx] > 1:
            return float('inf')
        elif c[idx] == 1:
            continue
        else:
            # find something!
            if sparePtr == -1:
                sparePtr = idx
                while c[sparePtr] == 0:
                    sparePtr -= 1
                    sparePtr %= n
            elif c[sparePtr] == 0:
                # ran out of spares, keep going
                while c[sparePtr] == 0:
                    sparePtr -= 1
                    sparePtr %= n
            # use one
            c[idx] += 1
            c[sparePtr] -= 1
            distance = min(abs(idx - sparePtr), abs(idx + n - sparePtr), abs(sparePtr + n - idx))
            cost += distance ** 2
    return cost

ans = float('inf')
for i in range(n):
    if cows[i] == 0:
        # make the last gap to fill be i
        ans = min(ans, checkEnd(i))
assert ans != float('inf')
print(ans)

'''
instead of mapping cows to sinks, 
what if we look at each sink and have it take the closest cow?

crazy observation, move everything 1 over then drop the cow into the door
ex. 20 cows to be moved from 100 to 101 spaces.
supposed optimal way: 20*201
other way: 21**2
oh, at some point it does become more efficient to not move each cow anymore
HMM

OK, I have a strat
claim: when trying ending at each gap, if there's inefficiency in any way, it's not the optimal one
    here we can continue
in that case, use 2P to greedily fill in, see where we end up

claim looks to be incorrect, in that case let's try making every cell the last hole
'''
