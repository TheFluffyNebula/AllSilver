# gpt fenwick implementation
import sys
# sys.stdin = open("running.in")
input = sys.stdin.readline
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.fw = [0]*(n+1)
    def update(self, i, v=1):
        while i <= self.n:
            self.fw[i] += v
            i += i & -i
    def query(self, i):
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s
    def range_sum(self, l, r):
        return self.query(r) - self.query(l-1)

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

# full version: deal w/ the floats 
# tree, how many the cow get/don't get the extra lap -- yes = normal ints, no = -1 for each
ints = [int(lapsRan[i]) for i in range(n)]

res_list = []
for i in range(n):
    residue = int((lapsRan[i] - ints[i]) * 1e9 + 0.5)
    res_list.append(residue)

vals = sorted(set(res_list))
comp = {v:i+1 for i,v in enumerate(vals)}  # 1-indexed

fw = Fenwick(len(vals))
inserted_count = 0

ans = 0
tot = 0

for i in range(n):
    if i > 0:
        toMatch = i * ints[i]
        toAdd = toMatch - tot
        
        # compressed index of current residue
        r = comp[res_list[i]]
        
        # how many residues > current residue?
        num_le = fw.query(r)         # ≤ current
        num_greater = inserted_count - num_le

        toAdd -= num_greater
        ans += toAdd

    tot += ints[i]

    # insert current residue
    fw.update(comp[res_list[i]])
    inserted_count += 1
print(ans)

'''
ints only: ex. 0 0 2 --> (2 * 2) = 4 - 0 = 4
total match - pf
'''
