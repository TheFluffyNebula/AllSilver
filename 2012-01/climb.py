import sys
# sys.stdin = open("climb.in")
input = sys.stdin.readline

n = int(input())
cows = [tuple(map(int, input().split())) for _ in range(n)]


fastUp = []
rem = []
for i in range(n):
    if cows[i][0] < cows[i][1]:
        fastUp.append(cows[i])
    else:
        rem.append(cows[i])
fastUp.sort()
rem.sort(key = lambda x: -x[1])
fastUp.extend(rem)
cows = fastUp

# start with the first cow at the top of the hill
t = cows[0][0]

# how much time going down remaining
down = cows[0][1]

for i in range(1, n):
    # print(idx)
    # cow climbs up
    t += cows[i][0]
    down = max(0, down - cows[i][0])
    down += cows[i][1]
print(t + down)

'''
how to promote maximum concurrency?
sol peek ._.
got the first part by myself
first, we want fast-up/slow-down cow
^^ u < d

so overall, increasing u then decreasing d
'''
