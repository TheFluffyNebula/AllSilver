import sys
sys.stdin = open("cowdance.in")
sys.stdout = open("cowdance.out", 'w')
from queue import PriorityQueue

n, t = map(int, input().split())
cows = [int(input()) for _ in range(n)]
# print(cows)

def check(k):
    # print("Checking", k)
    pq = PriorityQueue()
    curTime = 0
    for i in range(k):
        # print(cows[i])
        pq.put(curTime + cows[i])
    for i in range(k, n):
        pq.put(pq.get() + cows[i])
    ret = 0
    while not pq.empty():
        ret = max(ret, pq.get())
    return ret <= t

L = 1
R = n
ans = n
while L <= R:
    mid = (L + R) // 2
    if check(mid):
        ans = mid
        R = mid - 1
    else:
        L = mid + 1
print(ans)

'''
binary search on the value of k, then need to simulate
what's the most efficient way to simulate?
^^ pq probably?
O(n log(n) log(d))
'''
