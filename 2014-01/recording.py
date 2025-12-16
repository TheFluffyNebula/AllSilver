import sys
sys.stdin = open("recording.in")
sys.stdout = open("recording.out", 'w')
from queue import PriorityQueue

n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
intervals.sort(key = lambda x: x[1])
# print(intervals)

pq = PriorityQueue()
pq.put(0)
pq.put(0)

ans = 0
for i in range(n):
    x = pq.get()
    y = pq.get()
    # manual "upper_bound" on 2 elements
    if y <= intervals[i][0]:
        ans += 1
        pq.put(intervals[i][1])
        pq.put(x)
    else:
        if x <= intervals[i][0]:
            ans += 1
            pq.put(intervals[i][1])
            pq.put(y)
        else:
            pq.put(x)
            pq.put(y)
print(ans)
