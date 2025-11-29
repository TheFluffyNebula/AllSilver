import sys
sys.stdin = open("fuel.in")
sys.stdout = open("fuel.out", 'w')
input = sys.stdin.readline

n, g, b, d = map(int, input().split())
stations = [tuple(map(int, input().split())) for _ in range(n)]
stations.sort()
# print(stations)

# go to station 1
curFuel = b - stations[0][0]
if curFuel < 0:
    print(-1)
    exit()
curStation = 0
# now for the algorithm as described below
ans = 0
madeItToDestination = False
while curStation < n:
    curCost = stations[curStation][1]
    # search for something w/ less cost
    lessIdx = -1
    for i in range(curStation + 1, n):
        if stations[i][0] - stations[curStation][0] > g:
            break
        # this is a station we can get to, check its price
        if stations[i][1] < curCost:
            lessIdx = i
            break
    # print(curStation, lessIdx, ans)
    if lessIdx == -1:
        # no station w/ less cost, get a full tank here and go to the next station (or to finish if enough for that)
        if d - stations[curStation][0] <= g:
            # we can get to the finish, do that
            distanceToFinish = d - stations[curStation][0]
            # print(distanceToFinish, curFuel)
            fuelPurchased = max(distanceToFinish - curFuel, 0)
            ans += fuelPurchased * stations[curStation][1]
            madeItToDestination = True
            break
        if curStation == n - 1:
            # did not make it to the end, don't toggle status & output -1
            break
        # fill tank & go next station
        fuelPurchased = g - curFuel
        ans += fuelPurchased * stations[curStation][1]
        curFuel = g - (stations[curStation + 1][0] - stations[curStation][0])
        curStation += 1
    else:
        # print(curFuel)
        # fuel enough to barely go to the station w/ less cost!
        distance = stations[lessIdx][0] - stations[curStation][0]        
        # this statement could reveal small lapse in logic/WA, careful
        fuelPurchased = max(distance - curFuel, 0)
        curFuel += fuelPurchased - distance
        ans += fuelPurchased * stations[curStation][1]
        curStation = lessIdx
print(ans) if madeItToDestination else print(-1)
'''
some observations
want to fuel up when it's cheap, have barely enough to make it to cheaper
ofc, if dist between adjacent stations > tank then output -1

if following stations are more expensive, go full tank
if any following station is cheaper, barely make it there

1. if we can make it to a cheaper station, do that
2. if we can't, fill to a full tank and go to the next station
could set last station price to float('-inf') (placeholder variable)
or... explicit check for last-station-in-sight-and-no-cheaper-between

an edge case to look for:
* overflow ex. starting fuel could exceed gas tank capacity?

nvm, let's go!!!
'''
