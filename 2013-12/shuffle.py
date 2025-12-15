import sys
sys.stdin = open("shuffle.in")
sys.stdout = open("shuffle.out", 'w')

n, m, q = map(int, input().split())
ordering = [int(input()) for _ in range(m)]
# print(ordering)

def compose(r, a, b, n):
    for i in range(n):
        r[i] = a[b[i]]

# solution copy
x = [0] * n
y = [0] * n
pi = [0] * n

t = n - m + 1
for i in range(n):
    x[i] = i
    if i < m:
        pi[ordering[i] - 1] = i
    else:
        pi[i] = i

pi = pi[1:] + pi[:1]

max_bit = t.bit_length() - 1

for i in range(max_bit, -1, -1):
    compose(y, x, x, n)
    x = y.copy()
    if (t & 1 << i):
        compose(y, x, pi, n)
        x = y.copy()

queries = [int(input()) for _ in range(q)]
for i in range(q):
    print(x[(n + m - 1 - queries[i]) % n] + 1)

'''
:(
'''
