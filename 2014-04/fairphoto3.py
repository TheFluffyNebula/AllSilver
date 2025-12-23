import sys
sys.stdin = open("fairphoto.in")
# sys.stdout = open("fairphoto.out", 'w')

n = int(input())
cows = [input().split() for _ in range(n)]
cows = [(int(cows[i][0]), cows[i][1]) for i in range(n)]
cows.sort()
print(cows)

L = 1
R = n // 2
ans = 0
while L <= R:
    mid = (L + R) // 2

'''
first, compute prefix sums
for each entry (alternate odd/even, store separately)
    binary search on all opposite parity using suffix maximum
    ans = max(ans, candidate)
todo: for the first... toggle attempt?
'''
