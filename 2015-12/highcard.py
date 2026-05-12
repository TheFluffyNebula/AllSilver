import sys
sys.stdin = open("highcard.in")
sys.stdout = open("highcard.out", 'w')

n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()
occupied = [False] * (2 * n + 1)
for x in a:
    occupied[x] = True
b = []
for i in range(1, 2 * n + 1):
    if not occupied[i]:
        b.append(i)
# print(a, b)

ans = 0
bPtr = 0
for aPtr in range(n):
    while b[bPtr] < a[aPtr]:
        bPtr += 1
        if bPtr > n - 1:
            break
    if bPtr > n - 1:
        break
    ans += 1
    # use the card
    bPtr += 1
    if bPtr > n - 1:
        break
print(ans)
'''
2P/greedy, match b[i] to a[i] optimally
'''
