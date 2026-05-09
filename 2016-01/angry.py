import sys
sys.stdin = open("angry.in")
sys.stdout = open("angry.out", 'w')
input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()
# print(a)

def check(x):
    c = 0
    cur = 0
    for i in range(n):
        if cur < a[i]:
            c += 1
            cur = a[i] + 2 * x    
    return c <= k

L = 0
R = 10 ** 9
ans = -1
while L <= R:
    mid = (L + R) // 2
    if check(mid):
        ans = mid
        R = mid - 1
    else:
        L = mid + 1
print(ans)

'''
binary search on explosion distance
'''