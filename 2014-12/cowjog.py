import sys
sys.stdin = open("cowjog.in")
sys.stdout = open("cowjog.out", 'w')

n, t = map(int, input().split())
cows = [tuple(map(int, input().split())) for _ in range(n)]
cows.sort()
# print(cows)

ans = 0
cur = float('inf')
for i in range(n - 1, -1, -1):
    furthest = cows[i][0] + t * cows[i][1]
    if furthest < cur:
        cur = furthest
        ans += 1
print(ans)

'''
could tackle this problem by iterating in reverse order
"will cow i+1 catch up to cow i"
then if it does, move onwards
'''
