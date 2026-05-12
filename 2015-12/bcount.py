import sys
sys.stdin = open("bcount.in")
sys.stdout = open("bcount.out", 'w')

n, q = map(int, input().split())
cows = [int(input()) for _ in range(n)]
# 1-indexed
queries = [tuple(map(int, input().split())) for _ in range(q)]
# print(queries)

pf1, pf2, pf3 = [0], [0], [0]
c1, c2, c3 = 0, 0, 0
for i in range(n):
    if cows[i] == 1:
        c1 += 1
    elif cows[i] == 2:
        c2 += 1
    else:
        c3 += 1
    pf1.append(c1)
    pf2.append(c2)
    pf3.append(c3)

for a, b in queries:
    print(pf1[b] - pf1[a - 1], pf2[b] - pf2[a - 1], pf3[b] - pf3[a - 1])
