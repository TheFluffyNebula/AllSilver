# Claude
# intuition: left inclusive, right exclusive, +1 built in
import sys
sys.stdin = open("haybales.in")
sys.stdout = open("haybales.out", 'w')
from bisect import bisect_left, bisect_right

n, q = map(int, input().split())
bales = list(map(int, input().split()))
bales.sort()

def query(start, end):
    lo = bisect_left(bales, start)   # first index with bales[i] >= start
    hi = bisect_right(bales, end)    # first index with bales[i] > end
    return hi - lo

for _ in range(q):
    a, b = map(int, input().split())
    print(query(a, b))
