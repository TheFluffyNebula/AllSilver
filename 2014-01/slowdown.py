import sys
sys.stdin = open("slowdown.in")
sys.stdout = open("slowdown.out", 'w')

n = int(input())

times = []
distances = []
for i in range(n):
    op, x = input().split()
    x = int(x)
    if op == 'T':
        times.append(x)
    else:
        distances.append(x)
times.sort()
distances.sort()
total_times = len(times)
total_distances = len(distances)
# print(times, distances)

curD = 0
curT = 0
# this is equivalent to i + 1
paceDenominator = 1
tPtr = 0
dPtr = 0

i = 0
while i < n:
    dVal = float('inf')
    tVal = float('inf')
    if tPtr < total_times:
        nextTime = times[tPtr]
        # what's the distance at which we reach this time?
        distanceTraveled = (nextTime - curT) * (1 / paceDenominator)
        tVal = curD + distanceTraveled
    if dPtr < total_distances:
        nextDistance = distances[dPtr]
        dVal = nextDistance

    newT = curT + (min(tVal, dVal) - curD) / (1 / paceDenominator)

    if tVal <= dVal:
        i += 1
        paceDenominator += 1
        tPtr += 1
    
    if dVal <= tVal:
        i += 1
        paceDenominator += 1
        dPtr += 1
    
    curD = min(tVal, dVal)
    curT = newT
    # print(curD)

remainingDistance = 1000 - curD
curT += remainingDistance / (1 / paceDenominator)
print(round(curT))
