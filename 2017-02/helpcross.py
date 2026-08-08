# :(
import sys
sys.stdin = open("helpcross.in")
# sys.stdout = open("helpcross.out", 'w')

c, n = map(int, input().split())
chickens = [int(input()) for _ in range(c)]
cows = [tuple(map(int, input().split())) for _ in range(n)]
cows.sort()
chickens.sort()
# print(cows, chickens)

# ans = 0
# L = 0
# for R in range(n):
#     while chickens[L] < cows[R][0]:
#         L += 1
#         if L >= c:
#             break
#     if L >= c:
#         break
#     if cows[R][0] <= chickens[L] <= cows[R][1]:
#         ans += 1
#         L += 1
#     if L >= c:
#         break
# print(ans)

'''
I think matching the chickens makes more sense here since they're more restricted
sort ofc (default order should be good, want earliest start and then end time)
    ex. (2, 5) should be taken over (2, 6)
peeked the solution
'''
