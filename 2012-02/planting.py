import sys
# sys.stdin = open("planting.in")
input = sys.stdin.readline

n = int(input())
rectangles = [tuple(map(int, input().split())) for _ in range(n)]
# upper left, lower right corners, sort by x value
rectangles.sort(key = lambda x: (-x[1], x[0]))
# print(rectangles)
events = set()
for i in range(n):
    events.add(rectangles[i][0])
    events.add(rectangles[i][2])
events = sorted(list(events))
# print(events)

def curHeight():
    # merge intervals and return their sum
    # sorted at the beginning
    # print(ongoing)
    intervals = []
    currentInterval = ()
    for i in range(n):
        if ongoing[i]:
            if currentInterval == ():
                currentInterval = (rectangles[i][1], rectangles[i][3])
                continue
            # overlap
            if rectangles[i][1] >= currentInterval[1]:
                currentInterval = (currentInterval[0], min(currentInterval[1], rectangles[i][3]))
            else:
                # zero overlap, new interval needed
                intervals.append(currentInterval)
                currentInterval = (rectangles[i][1], rectangles[i][3])
    if currentInterval:
        intervals.append(currentInterval)
    # print(intervals)
    tot = 0
    for i in range(len(intervals)):
        tot += intervals[i][0] - intervals[i][1]
    return tot

ans = 0
# track what intervals are being swept over
ongoing = [False] * (n)
for (i, e) in enumerate(events):
    # progress and take events out of the height
    duration = e - events[i - 1]
    ans += duration * curHeight()
    for j in range(n):
        if rectangles[j][2] == e:
            ongoing[j] = False

    # put events in
    for j in range(n):
        if rectangles[j][0] == e:
            ongoing[j] = True
print(ans)

'''
"sweep line algorithm"
A we encounter interesting events, process them
I think I know what that means now!
It's like stuck in a rut but easier

so, first step would be to sort and then we can track the 1000 things for the 2000 events that happen

ex. (0, 5, 4, 1)
x=0 to x=4, y=1 to y=5 covered, +1 for inclusive intervals
x . . . .
. . . . .
. . . . .
. . . . .
. . . . x
. . . . .
'''
