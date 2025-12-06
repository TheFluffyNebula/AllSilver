import sys
sys.stdin = open("msched.in")
sys.stdout = open("msched.out", 'w')
from queue import PriorityQueue

n = int(input())
cows = [tuple(map(int, input().split())) for _ in range(n)]
cows.sort(key=lambda x: (x[1]), reverse=True)
# print(cows)

pq = PriorityQueue()
p = 0
ans = 0
for t in range(10000, 0, -1):
    # last time tick is t=1
    if p <= n - 1:
        while cows[p][1] >= t:
            # print("hi")
            # force max pq
            pq.put(-cows[p][0])
            p += 1
            if p == n:
                break
    if not pq.empty():
        ans += -pq.get()
print(ans)

'''
not quite just taking the max at each time
what if we go backwards?
backwards & priority queue
each cow becomes available at time cows[i][1]
'''
