import sys
sys.stdin = open("div7.in")
sys.stdout = open("div7.out", 'w')
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

pf = [0]
cur = 0
for i in range(n):
    pf.append(pf[-1] + a[i])

# 1 per residue mod 7
earliest = [-1] * 7
best = 0
for i in range(n):
    if earliest[pf[i] % 7] == -1:
        earliest[pf[i] % 7] = i
    best = max(best, i - earliest[pf[i] % 7])    
print(-1) if best == 0 else print(best)

'''
prefix sums
same = solution
store earliest occurrence
take max
'''