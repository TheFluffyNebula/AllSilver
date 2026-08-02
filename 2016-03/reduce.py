import sys
sys.stdin = open("reduce.in")
sys.stdout = open("reduce.out", 'w')

def curArea(cords):
    cX, cY = zip(*cords)
    cX, cY = list(cX), list(cY)
    minX, minY = min(cX), min(cY)
    maxX, maxY = max(cX), max(cY)
    return (maxX - minX) * (maxY - minY)

def search(arr, elimsRemaining):
    global ans
    ans = min(ans, curArea(arr))
    if elimsRemaining == 0:
        return
    # look for possible eliminations
    cX, cY = zip(*arr)
    cX, cY = list(cX), list(cY)
    minX, minY = min(cX), min(cY)
    maxX, maxY = max(cX), max(cY)
    # cut ?
    left = cX.count(minX)
    right = cX.count(maxX)
    bot = cY.count(minY)
    top = cY.count(maxY)
    if elimsRemaining >= left:
        restore = []
        for i in range(len(arr) - 1, -1, -1):
            if arr[i][0] == minX:
                restore.append(arr.pop(i))
        search(arr, elimsRemaining - left)
        arr.extend(restore)
    if elimsRemaining >= right:
        restore = []
        for i in range(len(arr) - 1, -1, -1):
            if arr[i][0] == maxX:
                restore.append(arr.pop(i))
        search(arr, elimsRemaining - right)
        arr.extend(restore)     
    if elimsRemaining >= bot:
        restore = []
        for i in range(len(arr) - 1, -1, -1):
            if arr[i][1] == minY:
                restore.append(arr.pop(i))
        search(arr, elimsRemaining - bot)
        arr.extend(restore)
    if elimsRemaining >= top:
        restore = []
        for i in range(len(arr) - 1, -1, -1):
            if arr[i][1] == maxY:
                restore.append(arr.pop(i))
        search(arr, elimsRemaining - top)
        arr.extend(restore)

n = int(input())
cords = [tuple(map(int, input().split())) for _ in range(n)]
# print(cords)

ans = float('inf')
search(cords, 3)
print(ans)

'''
observations:
area is defined by (maxX - minX) * (maxY - minY)
this we need to increase the min or reduce the max

very particular ways to reduce areas w/ 3 different cows
sometimes remove one can help one or even both dimensions

sometimes we need to remove 3 in a row to get going
> casework?
ex. 3 is easy, adjust one of 4 dimensions

ooh, on that note there are only so many levers we can pull and only so many depths we can go
each dimensions has a cost to reduce, 1 2 or 3 cows removed
worst case scenario is going 3 levels deep
4**3 = 64, just try every permutation of removing cows!
triple loop, done?

I guess the bookkeeping might get hazy
meh, 64 * 50000 is still fine
not even 64 since it's more like 4C3 w/ repetition
3 stars, 3 bars, C(6, 3) = 20
simplest implementation might be recursive search (will be full 64)
I forgot how to do backtracking >.<
'''
