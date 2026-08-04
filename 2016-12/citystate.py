import sys
sys.stdin = open("citystate.in")
sys.stdout = open("citystate.out", 'w')
from collections import defaultdict

n = int(input())
places = [tuple(input().split()) for _ in range(n)]
places = [(places[i][0][:2], places[i][1]) for i in range(n)]
# print(places)
ans = 0
d = defaultdict(int)
for i in range(n):
    if places[i][0] != places[i][1]:
        ans += d[(places[i][1], places[i][0])]
        d[places[i]] += 1
print(ans)
