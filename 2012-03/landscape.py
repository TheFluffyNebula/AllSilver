# incorrect
import sys
# sys.stdin = open("landscape.in")
input = sys.stdin.readline

n, x, y, z = map(int, input().split())
a = []
for i in range(n):
    c, b = map(int, input().split())
    a.append(c - b)
# print(a, sum(a))

ans = 0
# for every slot, do the following...
for i in range(n):
    if a[i] == 0:
        continue
    for j in range(i + 1, n):
        # needs additional, pull from positive only
        if a[i] < 0:
            if a[j] > 0:
                units = min(abs(a[i]), abs(a[j]))
                # key assumption: one of these two operations is always going to be optimal
                zCost = abs(i - j) * units
                xyCost = (x + y) * units
                ans += min(zCost, xyCost)
                a[i] += units
                a[j] -= units
        else:
            # needs less, move to negative only
            if a[j] < 0:
                units = min(abs(a[i]), abs(a[j]))
                # key assumption: one of these two operations is always going to be optimal
                zCost = abs(i - j) * units
                xyCost = (x + y) * units
                ans += min(zCost, xyCost)
                a[i] -= units
                a[j] += units
        if a[i] == 0:
            break
        # if it still needs help then we finish it off with filling/removing
    if a[i] < 0:
        ans += x * abs(a[i])
    else:
        ans += y * a[i]
    a[i] = 0
print(ans)

'''
make difference array to see what operations are needed
the z-operation should clearly be used by pots that are the closest (greedy)
go in order, left to right

actually, operation comparison
simplest case: move one block of soil one spot
z-operation 1 over = z
alternatively, x + y

observation: we never want to add + move -- at that point just add at the location

in the example, we have [-3, -1, 1, 4]
we can 'greedily' pull the positives over to the negatives
left: [0, 0, 0, 1] <-- remove this one
what does the opposite look like? if positive, pull the closest negatives
left to right approach should be fine

for each 'greedy pull', consider x + y vs. z * distance cost per block
'''
