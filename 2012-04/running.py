import sys
# sys.stdin = open("running.in")
input = sys.stdin.readline
import bisect

n, l, c = map(int, input().split())
speeds = [int(input()) for _ in range(n)]
speeds.sort()
# print(speeds)

raceTime = l * c / speeds[-1]
lapsRan = []
for i in range(n):
    laps = raceTime * speeds[i] / c
    lapsRan.append(laps)
# print(lapsRan)

# easier version : integer amts
# ints = [int(lapsRan[i]) for i in range(n)]
# intsOnly = 0
# tot = 0
# for i in range(n):
#     if i > 0:
#         toMatch = i * ints[i]
#         intsOnly += toMatch - tot
#     tot += ints[i]
# print(intsOnly)

# full version: deal w/ the floats 
# tree, how many the cow get/don't get the extra lap -- yes = normal ints, no = -1 for each
ints = [int(lapsRan[i]) for i in range(n)]
residues = []
ans = 0
tot = 0
for i in range(n):
    if i > 0:
        toMatch = i * ints[i]
        toAdd = toMatch - tot
        pos = bisect.bisect(residues, int(round((lapsRan[i] - ints[i]) * 10 ** 9)))
        num_greater = len(residues) - pos
        # print(residues, num_greater)
        toAdd -= num_greater
        ans += toAdd
        # print(toAdd)
    tot += ints[i]
    bisect.insort(residues, int(round((lapsRan[i] - ints[i]) * 10 ** 9)))
print(ans)

'''
ints only: ex. 0 0 2 --> (2 * 2) = 4 - 0 = 4
total match - pf
'''
