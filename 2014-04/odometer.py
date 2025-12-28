# proud of myself for this one!
import sys
sys.stdin = open("odometer.in")
sys.stdout = open("odometer.out", 'w')
from functools import lru_cache

low, high = input().split()
lowTotal = len(low)
highTotal = len(high)
lowList = list(low)
highList = list(high)
# low, high = int(low), int(high)

def search(n, majorityDigit, initialConditions):
    @lru_cache(None)
    def searchRecursive(i, c, conditions):
        # got to the end
        if i == n:
            if c >= (n + 1) // 2:
                return 1
            # this line should never trigger
            return 0
        L = 0
        R = 9
        if i == 0:
            L = 1
        if not conditions & 2:
            # bound by lower
            L = int(lowList[i])
        if not conditions & 1:
            # bound by higher
            R = int(highList[i])
        ret = 0
        for j in range(L, R + 1):
            # good for low and good for high
            newGFL = conditions & 2
            if j > L:
                newGFL = 2
            newGFH = conditions & 1
            if j < R:
                newGFH = 1
            newConditions = newGFL | newGFH | conditions
            if j == majorityDigit:
                ret += searchRecursive(i + 1, c + 1, newConditions)
            else:
                ret += searchRecursive(i + 1, c, newConditions)
        return ret    
    return searchRecursive(0, 0, initialConditions)

def duplicates(n, dup1, dup2, initialConditions):
    # here we'll let j equal first digit (aka i when called in the for loop)
    @lru_cache(None)
    def duplicateRecursive(i, c, conditions):
        # got to the end
        if i == n:
            # need exactly half of each
            if c == n // 2:
                return 1
            return 0
        L = 0
        R = 9
        if i == 0:
            L = 1
        if not conditions & 2:
            # bound by lower
            L = int(lowList[i])
        if not conditions & 1:
            # bound by higher
            R = int(highList[i])
        ret = 0
        for j in range(L, R + 1):
            if j != dup1 and j != dup2:
                continue
            # good for low and good for high
            newGFL = conditions & 2
            if j > L:
                newGFL = 2
            newGFH = conditions & 1
            if j < R:
                newGFH = 1
            newConditions = newGFL | newGFH | conditions
            if j == dup1:
                ret += duplicateRecursive(i + 1, c + 1, newConditions)
            else:
                # j is dup2
                ret += duplicateRecursive(i + 1, c, newConditions)
        return ret    
    return duplicateRecursive(0, 0, initialConditions)

ans = 0
for digitCount in range(3, 20):
    if digitCount < lowTotal or digitCount > highTotal:
        continue
    
    # good-for-low = 2, good-for-high = 1
    bounds = 0
    if digitCount > lowTotal:
        bounds += 2
    if digitCount < highTotal:
        bounds += 1

    for majorityDigit in range(10):
        # number of digits, majority digit, good-for-low/good-for-high
        ans += search(digitCount, majorityDigit, bounds)
        # print(majorityDigit, search(digitCount, majorityDigit, bounds))
    
    # subtract duplicates (ex. 2244 w/ 2 & 4 as majority digits)
    if digitCount % 2 == 0:
        for i in range(10):
            for j in range(i + 1, 10):
                ans -= duplicates(digitCount, i, j, bounds)

print(ans)

'''
the only option I see here is mathematical computation
perhaps we can shortcut some of the intermediate digits
brute force each as majority digit --> overlap possible?
ex. 2244 on both 2 and 4 as majority digit

for that we can use PIE (subtract duplicates when even digits)
when considering low and high, only apply restrictions when same number of digits

to consider: early pruning via i + c < n
'''
