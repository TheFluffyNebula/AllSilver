# module doesn't exist
import sys
# sys.stdin = open("fpot.in")
input = sys.stdin.readline
from sortedcontainers import SortedList

n, d = map(int, input().split())
drops = [tuple(map(int, input().split())) for _ in range(n)]
drops.sort()
# print(drops)


best = float('inf')
sl = SortedList()
L = 0
for R in range(n):
    # sort/query by height
    # (height, x-value)
    sl.add((drops[R][1], drops[R][0]))
    while sl[-1][0] - sl[0][0] >= d:
        # print(sl)
        best = min(best, abs(sl[-1][1] - sl[0][1]))
        sl.remove((drops[L][1], drops[L][0]))
        L += 1
print(best) if best != float('inf') else print(-1)

'''
2 pointers!
move R until good, then move L inward for min distance
Standard Tree would be work -- log n for both operations, one 2P pass and done
some alternatives -- segment tree, sqrt root decomposition, sparse table
'''
'''
class SegmentTree:
    def __init__(self, n):
        # amount of leaf nodes
        self.size = 2 ** math.ceil(math.log2(n))
        # make space for internal nodes as well (1 extra slot)
        self.mins = [float('inf')] * (2 * self.size)
    
    def build_segment(self, a, x, lx, rx):
        if rx - lx  == 1:
            if lx < len(a):
                self.mins[x] = a[lx]
            return
        m = (lx + rx) // 2
        self.build_segment(a, 2 * x + 1, lx, m)
        self.build_segment(a, 2 * x + 2, m, rx)
        self.mins[x] = min(self.mins[2 * x + 1], self.mins[2 * x + 2])

    def build_all(self, a):
        self.build_segment(a, 0, 0, self.size)
    
    # i is the original (array) index we want to update
    # x is where we are in the tree
    # lx & rx represent the left and right indices of the function
    def set_segment(self, i, v, x, lx, rx):
        if rx - lx == 1:
            self.mins[x] = v
            return
        m = (lx + rx) // 2
        if i < m:
            self.set_segment(i, v, 2 * x + 1, lx, m)
        else:
            self.set_segment(i, v, 2 * x + 2, m, rx)
        self.mins[x] = min(self.mins[2 * x + 1], self.mins[2 * x + 2])
        
    def set_all(self, i, v):
        self.set_segment(i, v, 0, 0, self.size)
    
    def min_segment(self, l, r, x, lx, rx):
        # outside the segment, return default value
        if lx >= r or rx <= l:
            return float('inf')
        # inside the segment, return the sume
        if lx >= l and rx <= r:
            return self.mins[x]
        # neither, recursion deeper
        m = (lx + rx) // 2
        s1 = self.min_segment(l, r, 2 * x + 1, lx, m)
        s2 = self.min_segment(l, r, 2 * x + 2, m, rx)
        return min(s1, s2)
    
    def min_all(self, l, r):
        return self.min_segment(l, r, 0, 0, self.size)
'''